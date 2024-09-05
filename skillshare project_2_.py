from datetime import datetime
from zoneinfo import ZoneInfo

def convert_time_zone(time_str, from_tz, to_tz):
    try:
        fmt = '%Y-%m-%d %H:%M:%S'
        
        naive_time = datetime.strptime(time_str, fmt)
        
        localized_time = naive_time.replace(tzinfo=ZoneInfo(from_tz))
    
        converted_time = localized_time.astimezone(ZoneInfo(to_tz))
        
        return converted_time.strftime(fmt)
    
    except Exception as e:
        return f"Error: {e}"

time_str = "2024-08-21 16:00:00" 
from_tz = "Asia/Tokyo"          
to_tz = "America/Los_Angeles" 

converted_time = convert_time_zone(time_str, from_tz, to_tz)
print(f"Converted time: {converted_time}")
