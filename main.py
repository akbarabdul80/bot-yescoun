import time

import requests

# URL dan Header
base_url = "https://bi.yescoin.gold/mission"
headers = {
    "token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNDAzNDM1ODkxIiwiY2hhdElkIjoiMTQwMzQzNTg5MSIsImlhdCI6MTczNDUzMjg3MiwiZXhwIjoxNzM3MTI0ODcyLCJyb2xlQXV0aG9yaXplcyI6W10sInVzZXJJZCI6MTg2NjA3MTEzODk2Nzc0ODYwOH0.081CT0ZuPddvzzF2Tc2K7680KjN55ZFBE9uLi1A_SzKU-vB9KogMF0lNdJbleNM6uzmLEDQX-MBgxLL_603YdQ",
    "Content-Type": "application/json"
}


def get_daily_missions():
    """Mengambil daftar misi harian."""
    url = f"{base_url}/getDailyMission"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get("code") == 0:  # Memastikan respons sukses
            return data.get("data", [])
        else:
            print(f"Error: {data.get('message')}")
            return []
    else:
        print(f"Request failed with status code: {response.status_code}")
        return []


def click_daily_mission(mission_id):
    """Melakukan klik misi harian berdasarkan missionId."""
    url = f"{base_url}/clickDailyMission"
    response = requests.post(url, headers=headers, data=str(mission_id))

    if response.status_code == 200:
        data = response.json()
        if data.get("code") == 0:
            print(f"Mission ID {mission_id}: Success - {data.get('message')}")
        else:
            print(f"Mission ID {mission_id}: Failed - {data.get('message')}")
    else:
        print(f"Mission ID {mission_id}: Request failed with status code {response.status_code}")


def check_daily_mission(mission_id):
    """Mengecek status misi harian berdasarkan missionId."""
    url = f"{base_url}/checkDailyMission"
    response = requests.post(url, headers=headers, data=str(mission_id))

    if response.status_code == 200:
        data = response.json()
        if data.get("code") == 0:
            print(f"Mission ID {mission_id}: {data.get('message')}")
        else:
            print(f"Mission ID {mission_id}: Failed - {data.get('message')}")
    else:
        print(f"Mission ID {mission_id}: Request failed with status code {response.status_code}")


def claim_reward(mission_id):
    """Mengklaim hadiah misi harian berdasarkan missionId."""
    url = f"{base_url}/claimReward"
    response = requests.post(url, headers=headers, data=str(mission_id))

    if response.status_code == 200:
        data = response.json()
        if data.get("code") == 0:
            print(f"Mission ID {mission_id}: {data.get('message')}")
        else:
            print(f"Mission ID {mission_id}: Failed - {data.get('message')}")
    else:
        print(f"Mission ID {mission_id}: Request failed with status code {response.status_code}")


def main():
    """Fungsi utama untuk mengambil misi dan mengkliknya satu per satu."""
    missions = get_daily_missions()
    if not missions:
        print("No missions found.")
        return

    for mission in missions:
        mission_id = mission.get("missionId")
        if mission_id:
            click_daily_mission(mission_id)
            time.sleep(1)
            check_daily_mission(mission_id)
            time.sleep(1)
            claim_reward(mission_id)
            time.sleep(1)
        else:
            print("Invalid mission data, skipping...")


if __name__ == "__main__":
    main()
