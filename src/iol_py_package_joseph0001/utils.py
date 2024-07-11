


def presentar_resultados_estado(estado):
    # Presentar el estado de cuenta de manera estructurada
    print(
        f'\nEstado de cuenta nº: {estado["cuentas"][0]["numero"]}',
        f'\n\t\t\t\t[Total en Pesos: ${estado["totalEnPesos"]}]\n',
        f'\nCuenta {estado["cuentas"][0]["tipo"]}',
        f'\t[Total: ${estado["cuentas"][0]["total"]}]\n',
        f'\n\t\tActivos Valorizados\t\t\t${estado["cuentas"][0]["titulosValorizados"]}',
        f'\n\t\tComprometido\t\t\t\t${estado["cuentas"][0]["comprometido"]}',
        f'\n\t\tDisponible para operar\t\t\t${"{:.2f}".format(sum(saldo["saldo"] for saldo in estado["cuentas"][0]["saldos"]) - estado["cuentas"][0]["comprometido"])}',
        f'\n\t\tDisponible en cuenta\t\t\t${"{:.2f}".format(estado["cuentas"][0]["disponible"])}',
        f'\n\t\t\tSaldo a acreditarse (Inmediato) $ {estado["cuentas"][0]["saldos"][1]["saldo"]}',
        f'\n\t\t\tSaldo a acreditarse (24hs)\t$ {estado["cuentas"][0]["saldos"][0]["saldo"]}',
        f'\n\t\t\tSaldo a acreditarse (48hs)\t$ {estado["cuentas"][0]["saldos"][1]["saldo"]}',
        f'\n\t\t\tSaldo a acreditarse (72hs)\t$ {estado["cuentas"][0]["saldos"][2]["saldo"]}',
        f'\n\t\t\tSaldo a acreditarse (+72hs)\t$ {estado["cuentas"][0]["saldos"][3]["saldo"]}',
        f'\n\nCuenta {estado["cuentas"][1]["tipo"]}',
        f'\t[Total: U$S {estado["cuentas"][1]["total"]}]\n',
        f'\n\t\tActivos Valorizados\t\t\tU$S {estado["cuentas"][1]["titulosValorizados"]}',
        f'\n\t\tComprometido\t\t\t\tU$S {estado["cuentas"][1]["comprometido"]}',
        f'\n\t\tDisponible para operar\t\t\tU$S {"{:.4f}".format(sum(saldo["saldo"] for saldo in estado["cuentas"][1]["saldos"][1:]) - estado["cuentas"][1]["comprometido"])}',
        f'\n\t\tDisponible en cuenta\t\t\tU$S {estado["cuentas"][1]["disponible"]}',
        f'\n\t\t\tSaldo a acreditarse (Inmediato) U$S {estado["cuentas"][1]["saldos"][1]["saldo"]}',
        f'\n\t\t\tSaldo a acreditarse (24hs)\tU$S {estado["cuentas"][1]["saldos"][0]["saldo"]}',
        f'\n\t\t\tSaldo a acreditarse (48hs)\tU$S {estado["cuentas"][1]["saldos"][1]["saldo"]}',
        f'\n\t\t\tSaldo a acreditarse (72hs)\tU$S {estado["cuentas"][1]["saldos"][2]["saldo"]}',
        f'\n\t\t\tSaldo a acreditarse (+72hs)\tU$S {estado["cuentas"][1]["saldos"][3]["saldo"]}\n',
    )
