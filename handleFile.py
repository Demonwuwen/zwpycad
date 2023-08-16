def handlNetUnit(filePath):
    import os
    import pandas as pd

    # 创建新的Excel文件和Sheet
    output_file = "扩容升级板件安装槽位表.xlsx"
    output_sheet = "Sheet1"

    # 创建Excel Writer
    output_writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    workbook = output_writer.book
    worksheet = workbook.add_worksheet(output_sheet)
    os.getcwd()
    # 写入第一行表头
    header = ["环路名称", "网元名称", "设备型号", "板件型号", "槽位号", "备注"]
    for col, header_text in enumerate(header):
        worksheet.write(0, col, header_text)

    # 寻找并处理“单板报表”文件

    network_element_files = [filename for filename in os.listdir(filePath) if "网元报表" in filename]

    for filename in network_element_files:
        file_path = os.path.join(filePath, filename)
        excel_data = pd.read_excel(file_path, header=None)

        # 初始化标志变量
        found_rows = False

        # 筛选满足条件的行
        excel_data[11] = pd.to_numeric(excel_data[11], errors='coerce')
        filtered_rows = excel_data[(excel_data[0] == result) & (excel_data[11] < 9)]

        # 如果发现满足条件的行，赋值给filtered_rows，并执行相应的操作
        if not filtered_rows.empty:
            found_rows = True
            # 复制数据到新的Excel文件
            for idx, row in filtered_rows.iterrows():
                data_to_copy = [row[0], row[8], row[1], row[11]]
                worksheet.write_row(worksheet.dim_rowmax + 1, 1, data_to_copy)

        # 如果找到了符合条件的行，则跳出外层循环
        if found_rows:
            break

    # 寻找并处理“网元报表”文件
    ne_report_files = [filename for filename in os.listdir(filePath) if "网元报表" in filename]

    for filename in ne_report_files:
        file_path = os.path.join(filePath, filename)
        excel_data = pd.read_excel(file_path, header=None)

        # 筛选满足条件的行
        filtered_rows = excel_data[excel_data[0] == "34-8726-高新西富士康D115G"]

        # 复制数据到新的Excel文件
        for idx, row in filtered_rows.iterrows():
            data_to_copy = [row[10]]
            worksheet.write_row(1, 0, data_to_copy)

    # 关闭Excel Writer
    output_writer._save()
