current_hour, current_min = input().split()
cook_time = int(input())

end_hour = (int(current_min) + cook_time) // 60 + int(current_hour)
end_min = (int(current_min) + cook_time) % 60

if end_min >= 60:
    end_hour += 1
    end_min -= 60

if end_hour >= 24:
    end_hour -= 24

print(f"{end_hour} {end_min}")
