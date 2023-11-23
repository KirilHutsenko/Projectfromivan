from pathlib import Path
import datetime

for f in Path('/Users/loklotl/Desktop').iterdir():
    if f.is_file():
        m_timestamp = f.stat().st_mtime
        m_time = datetime.date.\
            fromtimestamp(m_timestamp).strftime("%d-%m-%Y")
        print(f"Name: {f.name}\n"
              f"Size: {f.stat().st_size} bytes\n"
              f"Date of creation: {m_time}\n"
              f"Full path: {f.parent.absolute()}\n")
