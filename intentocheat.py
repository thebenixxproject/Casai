import ctypes
import keyword
import time
import random
import keyboard

class GTAVOnlineCheat:
    def __init__(self):
        self.money = 0
        self.level = 1
        self.casino_points = 0
        self.aimbot_enabled = False
        self.car_spawn_enabled = False

    def set_money(self, amount):
        self.money += amount
        print(f"Money set to: {self.money}")

    def set_level(self, level):
        if 1 <= level <= 8000:
            self.level = level
            print(f"Level set to: {self.level}")

    def set_casino_points(self, points):
        self.casino_points += points
        print(f"Casino points set to: {self.casino_points}")

    def toggle_aimbot(self):
        self.aimbot_enabled = not self.aimbot_enabled
        state = "enabled" if self.aimbot_enabled else "disabled"
        print(f"Aimbot {state}")

    def spawn_car(self, car_name):
        print(f"Spawning car: {car_name}")

    def gift_car(self, player_id, car_name):
        print(f"Gifting {car_name} to player {player_id}")

    def show_stats(self):
        fps = random.randint(30, 60)
        players_in_server = random.randint(1, 30)
        print(f"FPS: {fps}, Players in server: {players_in_server}")

    def command_menu(self):
        print("Press 'U' to open command menu")
        while True:
            if keyboard.is_pressed('u'):
                print("Command Menu:")
                print("1. Set Money")
                print("2. Set Level")
                print("3. Set Casino Points")
                print("4. Toggle Aimbot")
                print("5. Spawn Car")
                print("6. Gift Car")
                print("7. Show Stats")
                time.sleep(1)

    def run(self):
        self.command_menu()

if __name__ == "__main__":
    cheat = GTAVOnlineCheat()
    cheat.run()


