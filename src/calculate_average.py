#!/usr/bin/env python
##############################################################################
#
# A simple example of some of the features of the XlsxWriter Python module.
#
# Copyright 2013-2016, John McNamara, jmcnamara@cpan.org
#
import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('averages.xlsx')
worksheet = workbook.add_worksheet()

## Widen the first column to make the text clearer.
##worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
#bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Avg Value')

# Text with formatting.
#worksheet.write('A2', 'Values')

# Write some numbers, with row/column notation. put your values into here, a, b, etc. first value is the row, second value is the column.
worksheet.write(2, 0, a)
worksheet.write(3, 0, b)
worksheet.write(4, 0, c)
worksheet.write(5, 0, d)
worksheet.write(6, 0, e)

# Insert an image.
#worksheet.insert_image('B5', 'logo.png')

# Write a total using a formula.
worksheet.write(row, 1, 'Total', bold)
worksheet.write(row, 0, '=SUM(A2:A6)')

workbook.close()
