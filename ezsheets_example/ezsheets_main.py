import ezsheets

my_spreadsheet = ezsheets.Spreadsheet("14qJKtiAsj8K0GlbBPU5xgWS3ifCq4yX2eNczc-AK1LA")

curr_sheet = my_spreadsheet[0]
rows = curr_sheet.getRows()

rows[0][0] = "Title"
rows[0][1] = "Author"
rows[0][2] = "Price"

rows[1][0] = "Ender's Game"
rows[1][1] = "Orson Scott Card"
rows[1][2] = "7.99"

rows[2][0] = "Harry Potter"
rows[2][1] = "JK Rowling"
rows[2][2] = "18.99"


curr_sheet.updateRows(rows)