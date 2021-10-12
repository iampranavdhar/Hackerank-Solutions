budget,keybord,drivers = map(int,input().split())
keybord_prices = list(map(int,input().split()))
mouse_prices = list(map(int,input().split()))
keybord_prices.sort()
mouse_prices.sort()
final = []
for i in range(len(keybord_prices)):
    for j in range(len(mouse_prices)):
        if (keybord_prices[i]+mouse_prices[j]) <= budget:   #Taken this condition to break the complete process as the sum will be greater than the budjet for the next consecutive steps in that loop.
            final.append(keybord_prices[i]+mouse_prices[j])
        else:
            break
if not final:
    print(-1)
else:
    print(max(final))