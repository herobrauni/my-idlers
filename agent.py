# get all server infos
# get server from my-idlers (if it exists)
# update or create server
# get id and run yabs
# Add OS and Basic Yabs to Note

import sys
import socket
import subprocess
import urllib.error
import urllib.request
import json
import os
import stat


def get_cpu_cores():
    try:
        # Run lscpu and parse its output
        lscpu_output = subprocess.check_output(['lscpu']).decode('utf-8')
        for line in lscpu_output.split('\n'):
            if 'CPU(s)' == line.split(':')[0].strip():
                return int(line.split(':')[1].strip())
    except:
        return None


def get_ram():
    try:
        with open('/proc/meminfo', 'r') as f:
            for line in f.readlines():
                if line.startswith('MemTotal:'):
                    # Convert KB to GB
                    return int(line.split()[1]) // 1024
    except:
        return None


def get_disk_space():
    df_output = subprocess.check_output(['df', '/'], text=True)
    total_disk = 0
    for line in df_output.split('\n')[1:]:  # Skip header
        if line:
            # Convert from KB to GB
            total_disk = int(line.split()[1]) // (1024 * 1024)
            break
    return total_disk


def get_ipv4():
    try:
        req = urllib.request.Request(f"https://ipv4.icanhazip.com")
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8').strip()
    except:
        return None


def get_ipv6():
    try:
        req = urllib.request.Request(f"https://ipv6.icanhazip.com")
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8').strip()
    except:
        return None


def get_servers(url, apikey, hostname):
    headers = {
        'Authorization': f'Bearer {apikey}',
        'Accept': 'application/json'
    }
    req = urllib.request.Request(
        f"{url}/api/servers",
        headers=headers
    )

    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
    return next((server for server in data if server["hostname"].lower() == hostname.lower()), None)


def get_os_list(url, apikey):
    headers = {
        'Authorization': f'Bearer {apikey}',
        'Accept': 'application/json'
    }
    req = urllib.request.Request(
        f"{url}/api/os",
        headers=headers
    )

    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))


def get_local_hostname():
    return socket.gethostname().lower()


def create_server(url, apikey, server_data):
    try:
        headers = {
            'Authorization': f'Bearer {apikey}',
            'Content-Type': 'application/json'
        }
        data = json.dumps(server_data).encode('utf-8')

        req = urllib.request.Request(
            f"{url}/api/servers",
            data=data,
            headers=headers,
            method='POST'
        )
        with urllib.request.urlopen(req) as response:
            print("\n✅ Server created successfully!")
            return json.loads(response.read().decode())
    except:
        return None


def update_server(url, apikey, server_data, server_id):
    try:
        dontuse = ["active", "bandwidth", "currency", "location_id", "next_due_date",
                   "owned_since", "payment_term", "price", "provider_id", "was_promo", "show_public", "ip1", "ip2", "ssh_port"]
        for du in dontuse:
            server_data.pop(du, None)
        headers = {
            'Authorization': f'Bearer {apikey}',
            'Content-Type': 'application/json'
        }

        data = json.dumps(server_data).encode('utf-8')

        req = urllib.request.Request(
            f"{url}/api/servers/{server_id}",
            data=data,
            headers=headers,
            method='PUT'
        )
        with urllib.request.urlopen(req) as response:
            print("\n✅ Server updated successfully!")
            return json.loads(response.read().decode())
    except:
        return None


def get_os_id(url, apikey):
    try:
        current_os = get_current_os()
        if not current_os:
            return None
            
        os_list = get_os_list(url, apikey)
        current_os_lower = current_os.lower()
        
        # First try exact match
        for os_item in os_list:
            if os_item['name'].lower() == current_os_lower:
                return int(os_item['id'])
        
        # Then try partial match
        for os_item in os_list:
            if current_os_lower in os_item['name'].lower():
                return int(os_item['id'])
        
        # If no match found, return ID for "None"
        return 1
    except:
        return 1  # Default to "None" if anything fails


def get_server_data(url, apikey):
    server_data = {
        "active": 1,
        "bandwidth": 1,
        "cpu": get_cpu_cores(),
        "currency": "EUR",
        "disk_as_gb": get_disk_space(),
        "disk_type": "GB",
        "disk": get_disk_space(),
        "hostname": get_local_hostname(),
        "location_id": 1,
        "next_due_date": "2025-01-01",
        "os_id": get_os_id(url, apikey),  # Replace the hardcoded 7 with dynamic OS detection
        "owned_since": "2024-01-01",
        "payment_term": 4,
        "price": 7,
        "provider_id": 1,
        "ram_as_mb": get_ram(),
        "ram_type": "GB",
        "ram": get_ram() >> 10,
        "server_type": 1,
        "show_public": 0,
        "ssh_port": 22,
        "was_promo": 1,
    }
    ipv4 = get_ipv4()
    ipv6 = get_ipv6()

    if ipv4 and ipv6:
        server_data["ip1"] = ipv4
        server_data["ip2"] = ipv6
    elif ipv4:
        server_data["ip1"] = ipv4
    elif ipv6:
        server_data["ip1"] = ipv6

    return server_data


def run_yabs(url, server_id, apikey):
    command = f'curl -sL yabs.sh | bash -s -- -96 -w yabs.json -s "{url}/api/yabs/{server_id}/{apikey}"'
    print(command)
    subprocess.run([command], shell=True)


def read_yabs_results():
    try:
        with open('yabs.json', 'r') as file:
            data = json.load(file)
            return {
                'isp': data.get('ip_info', {}).get('isp'),
                'asn': data.get('ip_info', {}).get('asn'),
                'org': data.get('ip_info', {}).get('org'),
                'city': data.get('ip_info', {}).get('city'),
                'country': data.get('ip_info', {}).get('country'),
                # Add more fields here as needed in the future
            }
    except FileNotFoundError:
        print("yabs.json not found - did the benchmark complete successfully?")
        return None
    except json.JSONDecodeError:
        print("Error parsing yabs.json - file may be corrupted")
        return None


def get_current_os():
    try:
        with open('/etc/os-release', 'r') as f:
            os_info = {}
            for line in f:
                if '=' in line:
                    key, value = line.rstrip().split('=', 1)
                    os_info[key] = value.strip('"')
            
            name = os_info.get('ID', '').lower()
            version = os_info.get('VERSION_ID', '')
            return f"{name} {version}".strip()
    except:
        return None


def get_note(url, apikey, server_id):
    headers = {
        'Authorization': f'Bearer {apikey}',
        'Accept': 'application/json'
    }
    req = urllib.request.Request(
        f"{url}/api/notes",
        headers=headers
    )

    try:
        with urllib.request.urlopen(req) as response:
            notes = json.loads(response.read().decode('utf-8'))
            note = next((note for note in notes if note["service_id"] == server_id), None)
            return note["id"] if note else None
    except:
        return None


def create_note(url, apikey, server_id, content):
    try:
        headers = {
            'Authorization': f'Bearer {apikey}',
            'Content-Type': 'application/json'
        }
        note_data = {
            'service_id': server_id,
            'note': content
        }
        data = json.dumps(note_data).encode('utf-8')

        req = urllib.request.Request(
            f"{url}/api/notes",
            data=data,
            headers=headers,
            method='POST'
        )
        with urllib.request.urlopen(req) as response:
            print("✅ Note created successfully!")
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Failed to create note: {str(e)}")
        return None


def update_note(url, apikey, server_id, content, id):
    try:
        headers = {
            'Authorization': f'Bearer {apikey}',
            'Content-Type': 'application/json'
        }
        note_data = {
            'service_id': server_id,
            'note': content
        }
        data = json.dumps(note_data).encode('utf-8')

        req = urllib.request.Request(
            f"{url}/api/notes/{server_id}",
            data=data,
            headers=headers,
            method='PUT'
        )
        with urllib.request.urlopen(req) as response:
            print("✅ Note updated successfully!")
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Failed to create note: {str(e)}")
        return None

if __name__ == "__main__":
    url, apikey = None, None
    try:
        url = str(sys.argv[1])
        apikey = str(sys.argv[2])
    except:
        if not url:
            url = input("Specify url: ")
        if not apikey:
            url = input("Specify apikey: ")
    server_data = get_server_data(url, apikey)

    if not (server := (get_servers(url, apikey, get_local_hostname()))):
        print("does not exist")
        server = create_server(url, apikey, server_data)
        print(server)
    else:
        print("does exist")
        server = update_server(url, apikey, server_data, server["id"])
        print(server["server_id"])

    run_yabs(url, server["server_id"], apikey)
    yabs_results = read_yabs_results()
    if yabs_results:
        print("YABS results loaded successfully")
        note_content = f"ISP: {yabs_results['isp']}\nASN: {yabs_results['asn']}\nORG: {yabs_results['org']}\nCity: {yabs_results['city']}\nCountry: {yabs_results['country']}"
    else:
        note_content = "yabs.json not found"
    if (note_id := get_note(url, apikey, server["server_id"])):
        print("Note exists ", note_id)
        update_note(url, apikey, server["server_id"], note_content, note_id)
    else:
        print("Note does not exist")
        create_note(url, apikey, server["server_id"], note_content)
