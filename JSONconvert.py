import json
import time



with open('nyheter/0.txt') as file, open('test.json', 'w') as json_file:
    items = {}
    for line in file:
        if not line.strip():
            continue
        data = line.split('|')
        for val in data:
            key, sep, value = val.partition(':')
            items[key.strip()] = value.strip()
    json.dump(items, json_file, indent=4)
    

print(items)

if __name__ == '__main__':
    while True:
        time_wait = 10
        print(f'Väntar {time_wait} minuter...')
        time.sleep(time_wait * 60)