import requests
import json
import pandas as pd
from datetime import datetime, timedelta
import os
from .utils import presentar_resultados_estado

### Variables de IOL
url_base = "https://api.invertironline.com/"

class IOL:
    
    def __init__(self, usuario, clave):
        self.user = usuario
        self.__password = clave
        self.__access = None
        self.__bearer = None
        self.__refresh = None
        self.__expiration = None
        self.__obtener_tokens()

    def __obtener_tokens(self):
        response = requests.post(
            url_base + "token",
            data={
                "username": self.user,
                "password": self.__password,
                "grant_type": "password"
            }
        )
        if response.status_code == 200:
            self.__access = response.json()
            self.__bearer = self.__access["access_token"]
            self.__refresh = self.__access["refresh_token"]
            self.__expiration = datetime.now() + timedelta(seconds=self.__access["expires_in"])
        else:
            raise Exception(f"No se pudo obtener el token. Código de estado: {response.status_code}")

    def refrescar_token(self):
        if not self.__refresh:
            raise Exception("No se ha obtenido un token de refresco previamente.")

        response = requests.post(
            url_base + "token",
            data={
                "refresh_token": self.__refresh,
                "grant_type": "refresh_token"
            }
        )
        if response.status_code == 200:
            self.__access = response.json()
            self.__bearer = self.__access["access_token"]
            self.__refresh = self.__access["refresh_token"]
            self.__expiration = datetime.now() + timedelta(seconds=self.__access["expires_in"])
        else:
            raise Exception(f"No se pudo refrescar el token. Código de estado: {response.status_code}")

    def obtener_bearer(self):
        if not self.__bearer or datetime.now() > self.__expiration:
            print("El token está vencido o próximo a vencer. Refrescando token...")
            self.refrescar_token()
        return {
            "Authorization": f"Bearer {self.__bearer}"
        }

    def obtener_estado_de_cuenta(self):
        try:
            headers = self.obtener_bearer()
            url = url_base + 'api/v2/estadocuenta'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                estado = response.json()
                presentar_resultados_estado(estado)
            else:
                print(f'Error en la solicitud: {response.status_code}')
        except Exception as e:
            print(f"Error en la solicitud: {e}")

    def mi_portafolio(self):
        try:
            headers = self.obtener_bearer()
            url = url_base + 'api/v2/portafolio/Argentina'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                portafolio = response.json()
                data = [{
                    'Descripción': activo['titulo']['descripcion'],
                    'Símbolo': activo['titulo']['simbolo'],
                    'Nominales': activo['cantidad'],
                    'Cotización': activo['ultimoPrecio'],
                    'Moneda': activo['titulo']['moneda'],
                    'Variación desde Compra (%)': activo['gananciaPorcentaje'],
                    'Valorizado': activo['valorizado'],
                    'Variación Diaria (%)': activo['variacionDiaria'],
                    'Ganancia Nominal': activo['gananciaDinero']
                } for activo in portafolio['activos']]
                df_mi_cuenta = pd.DataFrame(data)
                return df_mi_cuenta
            else:
                print(f'Error en la solicitud: {response.status_code}')
        except Exception as e:
            print(f"Error en la solicitud: {e}")

    def mis_operaciones(self, tipo='todas', fechadesde='2020-02-01', fechahasta='2024-07-01', pais='argentina'):
        try:
            headers= self.obtener_bearer()
            params = {
                'filtro.estado': tipo,
                'filtro.fechaDesde': fechadesde,
                'filtro.fechaHasta': fechahasta,
                'filtro.pais': pais
            }
            base_url = url_base + 'api/v2/operaciones'
            response = requests.get(base_url, headers=headers, params=params)
            if response.status_code == 200:
                operaciones = response.json()
                df_operaciones = pd.DataFrame(operaciones)
                return df_operaciones
            else:
                print(f"Error: {response.status_code}")
        except Exception as e:
            print(f"Error en la solicitud: {e}")

    def hist_precio(self, mercado='bcba', simbolo='ko', desde='2020-02-01', hasta='2024-07-01',ajustada='sinAjustar'):
        try:
            headers = self.obtener_bearer()
            url = f"{url_base}api/v2/{mercado}/Titulos/{simbolo}/Cotizacion/seriehistorica/{desde}/{hasta}/{ajustada}"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error en la solicitud: {e}")
            return None


