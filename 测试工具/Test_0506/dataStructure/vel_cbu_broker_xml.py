# coding:utf8

"""
功能名称：Broker报文生成工具--车辆生产CBU
作者：
创建时间：
"""
import datetime
import random
import time
from xml.dom.minidom import Document


def write(vin):
    doc = Document()
    root_node = doc.createElement("vehicleInformation")
    doc.appendChild(root_node)

    """vehicle"""
    vehicle = doc.createElement("vehicle")
    vehicle.setAttribute("vinLong", vin)
    root_node.appendChild(vehicle)

    # vehicle-status
    status = doc.createElement("status")
    status_value = doc.createTextNode('P')
    status.appendChild(status_value)
    vehicle.appendChild(status)

    # vehicle-f2Date
    f2Date = doc.createElement("f2Date")
    f2Date_value = doc.createTextNode(datetime.datetime.now().strftime('%d.%m.%y %H:%M:%S,%f' + '000'))
    f2Date.appendChild(f2Date_value)
    vehicle.appendChild(f2Date)

    # vehicle-m203Date
    m203date = doc.createElement("m203Date")
    m203date_value = doc.createTextNode(datetime.datetime.now().strftime('%d.%m.%y %H:%M:%S,%f' + '000'))
    m203date.appendChild(m203date_value)
    vehicle.appendChild(m203date)


    by_vin_match_1 = {'1Z21': 'i3 60Ah BEV', '1Z41': 'i3 60Ah REX', '1Z81': 'i3 94 REX', '1Z61': 'i3 94 Ah',
                    '7Z21':'i3 94Ah BEV', '7Z41': 'I01 i3 94Ah REX','8P21': 'I01 i3 120Ah', '2Z61': 'I15 i8 Roadster'}

    by_vin_match_2 = {'1Z21': 'i3', '1Z41': 'i3 REX', '1Z81': 'i3 REX', '1Z61': 'i3',
                    '7Z21':'i3', '7Z41': 'i3 REX','8P21': 'i3', '2Z61': 'i8'}

    vin_value = vin[3:7] # 截取VIN4-7位
    if vin_value in by_vin_match_1:
        # vehicle-vehicleModeldescription
        vmd = doc.createElement("vehicleModelDescription")
        vmd_value = doc.createTextNode(by_vin_match_1[vin_value])  # 使用VIN映射出车型描述
        vmd.appendChild(vmd_value)
        vehicle.appendChild(vmd)

        # vehicle-vehicleType
        # vt_value = random.choice(by_vin_match) # 随机取一个值
        vehicle_type = doc.createElement("vehicleType")
        vehicle_type_value = doc.createTextNode(vin_value) # 截取VIN4-7位作为车型
        vehicle_type.appendChild(vehicle_type_value)
        vehicle.appendChild(vehicle_type)

        # vehicle-bodyType
        body_type = doc.createElement("bodyType")
        body_type_value = doc.createTextNode(by_vin_match_2[vin_value]) # 使用VIN映射出车辆型号
        body_type.appendChild(body_type_value)
        vehicle.appendChild(body_type)
    else:
        print("VIN4-7位不符合规范")

    # vehicle-maintenanceDate
    maintenanceDate = doc.createElement("maintenanceDate")
    maintenanceDate_value = doc.createTextNode("")
    maintenanceDate.appendChild(maintenanceDate_value)
    vehicle.appendChild(maintenanceDate)

    # vehicle-maintenanceDealer
    maintenanceDealer = doc.createElement("maintenanceDealer")
    maintenanceDealer_value = doc.createTextNode("")
    maintenanceDealer.appendChild(maintenanceDealer_value)
    vehicle.appendChild(maintenanceDealer)

    # vehicle-maintenanceDealerName
    maintenanceDealerName = doc.createElement("maintenanceDealerName")
    maintenanceDealerName_value = doc.createTextNode("")
    maintenanceDealerName.appendChild(maintenanceDealerName_value)
    vehicle.appendChild(maintenanceDealerName)

    # vehicle-maintenanceDealerName
    destinationEnterpriseCode = doc.createElement("destinationEnterpriseCode")
    destinationEnterpriseCode_value = doc.createTextNode("")
    destinationEnterpriseCode.appendChild(destinationEnterpriseCode_value)
    vehicle.appendChild(destinationEnterpriseCode)

    """batterypack"""
    battery_pack = doc.createElement("batterypack")
    vehicle.appendChild(battery_pack)

    # batterypack-gtbcode
    bpgc = doc.createElement("batteryPackGBTCode")
    bpgc_value = doc.createTextNode("PACKGBTCODE")
    bpgc.appendChild(bpgc_value)
    battery_pack.appendChild(bpgc)

    # batterypack-bmwcode
    bpbc = doc.createElement("batteryPackBMWCode")
    bpbc_value = doc.createTextNode("PACKBMWCODE")
    bpbc.appendChild(bpbc_value)
    battery_pack.appendChild(bpbc)
    if vin_value =='2Z61':
        """循环插入包：模块：单体= 1:6:16"""
        # 外层循环模块
        for i in range(1, 7):
            """batterymodule"""
            battery_module = doc.createElement("batteryModul")
            battery_pack.appendChild(battery_module)

            # batterymodule-gtbcode
            bmgc = doc.createElement("batteryModulGBTCode")
            bmgc_value = doc.createTextNode('MODULEGBTCODE' + str(i))
            bmgc.appendChild(bmgc_value)
            battery_module.appendChild(bmgc)

            # batterymodule-bmwcode
            bmbc = doc.createElement("batteryModulBMWCode")
            bmbc_value = doc.createTextNode('MODULEBMWCODE' + str(i))
            bmbc.appendChild(bmbc_value)
            battery_module.appendChild(bmbc)

            # batterymodule-oldgbtcode
            obmgc = doc.createElement("oldBatteryModulGBTCode")
            obmgc_value = doc.createTextNode("")
            obmgc.appendChild(obmgc_value)
            battery_module.appendChild(obmgc)

            # batterymodule-oldbmwcode
            obmbc = doc.createElement("oldBatteryModulBMWCode")
            obmbc_value = doc.createTextNode("")
            obmbc.appendChild(obmbc_value)
            battery_module.appendChild(obmbc)

            # 内层循环单体(i-1)*12 +1 ,i*12+1
            for j in range((i-1)*16+1, i*16+1):
                """batterycell"""
                battery_cell = doc.createElement("batteryCell")
                battery_module.appendChild(battery_cell)

                bcgc = doc.createElement("batteryCellGBTCode")
                bcgc_value = doc.createTextNode("CELLGBTCODE" + str(j))
                bcgc.appendChild(bcgc_value)
                battery_cell.appendChild(bcgc)

                # batterymodule-bmwcode
                bcbc = doc.createElement("batteryCellBMWCode")
                bcbc_value = doc.createTextNode("CELLBMWCODE" + str(j))
                bcbc.appendChild(bcbc_value)
                battery_cell.appendChild(bcbc)

                # batterymodule-oldgtbcode
                obcgc = doc.createElement("oldBatteryCellGBTCode")
                obcgc_value = doc.createTextNode("")
                obcgc.appendChild(obcgc_value)
                battery_cell.appendChild(obcgc)

                # batterymodule-oldbmwcode
                obcbc = doc.createElement("oldBatteryCellBMWCode")
                obcbc_value = doc.createTextNode("")
                obcbc.appendChild(obcbc_value)
                battery_cell.appendChild(obcbc)
    else:
        """循环插入包：模块：单体= 1:8:12"""
        # 外层循环模块
        for i in range(1,9):
            """batterymodule"""
            battery_module = doc.createElement("batteryModul")
            battery_pack.appendChild(battery_module)

            #batterymodule-gtbcode
            bmgc = doc.createElement("batteryModulGBTCode")
            bmgc_value = doc.createTextNode('MODULEGBTCODE' + str(i))
            bmgc.appendChild(bmgc_value)
            battery_module.appendChild(bmgc)

            #batterymodule-bmwcode
            bmbc = doc.createElement("batteryModulBMWCode")
            bmbc_value = doc.createTextNode('MODULEBMWCODE' + str(i))
            bmbc.appendChild(bmbc_value)
            battery_module.appendChild(bmbc)

            #batterymodule-oldgbtcode
            obmgc = doc.createElement("oldBatteryModulGBTCode")
            obmgc_value = doc.createTextNode("")
            obmgc.appendChild(obmgc_value)
            battery_module.appendChild(obmgc)

            #batterymodule-oldbmwcode
            obmbc = doc.createElement("oldBatteryModulBMWCode")
            obmbc_value = doc.createTextNode("")
            obmbc.appendChild(obmbc_value)
            battery_module.appendChild(obmbc)

            # 内层循环单体
            for j in range((i-1)*12 +1 ,i*12+1):
                """batterycell"""
                battery_cell = doc.createElement("batteryCell")
                battery_module.appendChild(battery_cell)

                bcgc = doc.createElement("batteryCellGBTCode")
                bcgc_value = doc.createTextNode("CELLGBTCODE" + str(j))
                bcgc.appendChild(bcgc_value)
                battery_cell.appendChild(bcgc)

                #batterymodule-bmwcode
                bcbc = doc.createElement("batteryCellBMWCode")
                bcbc_value = doc.createTextNode("CELLBMWCODE" + str(j))
                bcbc.appendChild(bcbc_value)
                battery_cell.appendChild(bcbc)

                #batterymodule-oldgtbcode
                obcgc = doc.createElement("oldBatteryCellGBTCode")
                obcgc_value = doc.createTextNode("")
                obcgc.appendChild(obcgc_value)
                battery_cell.appendChild(obcgc)

                #batterymodule-oldbmwcode
                obcbc = doc.createElement("oldBatteryCellBMWCode")
                obcbc_value = doc.createTextNode("")
                obcbc.appendChild(obcbc_value)
                battery_cell.appendChild(obcbc)

    with open("vel_cbu_broker.xml", "w") as f:
        doc.writexml(f,indent = '\t',newl = '\n', addindent = '\t',encoding='utf-8')


if __name__ == '__main__':
    write('WBY2Z610000000001')