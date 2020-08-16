
def razon_circulante(
    activo_corriente, pasivo_corriente):
    return activo_corriente/pasivo_corriente

def prueba_de_acido(
    activo_corriente, pasivo_corriente, inventario):
    return (activo_corriente-inventario)/pasivo_corriente

def razon_de_rotacion_de_activos_fijos(
    ventas, activos_fijos_netos):
    return ventas/activos_fijos_netos

def razon_de_rotacion_de_activos_totales(
    ventas, activos_totales):
    return ventas/activos_totales

def rotacion_de_inventarios(
    costo_de_ventas, inventario):
    return costo_de_ventas/inventario

def dias_de_venta_pendientes_de_cobro(
    cuentas_por_cobrar, ventas_anuales):
    return cuentas_por_cobrar/(ventas_anuales/360)

def razon_de_deuda(
    deuda_total, total_activo):
    return deuda_total/total_activo

def razon_de_cobertura_de_intereses(
    utilidad_operativa, cargos_por_intereses):
    # utilidad operativa es la que va antes de impuestos e interese.
    return utilidad_operativa/cargos_por_intereses

def margen_de_utilidad_sobre_ventas(
    utilidad_neta_disp_para_accionistas, ventas 
    ):
    return utilidad_neta_disp_para_accionistas/ventas

def razon_de_rentabilidad_basica(
    utilidad_operativa, activo_total):
    return utilidad_operativa/activo_total

