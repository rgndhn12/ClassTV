from ClassTV import Tv

tv_one = Tv(30, 3, True)
tv_two = Tv(3, 2, False)

print(f"tv1's channel is {tv_one.get_channel()} and volume level is {tv_one.get_volume()}")
print(f"tv2's channel is {tv_two.get_channel()} and volume level is {tv_two.get_volume()}")




