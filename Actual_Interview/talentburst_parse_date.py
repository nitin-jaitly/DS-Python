from datetime import datetime

def transform_date_format(dates):
    result = []
    for date in dates:
        # Check if date string is already in format YYYYMMDD
        if len(date) == 8 and date.isdigit():
            continue
        else:
            try:
                for fmt in ['%Y/%m/%d','%d/%m/%Y','%m-%d-%Y']:
                    try:
                        ## Attempt to parse the date
                        parsed_date  = datetime.strptime(date, fmt)
                        parsed_date2 = parsed_date.strftime('%Y%m%d')
                        # Convert to YYYYMMDD
                        result.append(parsed_date2)
                        break
                    except ValueError:
                        continue
            except: # If date cannot be parsed
                continue
    print(f"result = {result}")
    return result

if __name__ == "__main__":
    dates = transform_date_format(["2010/02/20", "19/12/2016", "11-18-2012", "20130720"])
    print(*dates, sep='\n')