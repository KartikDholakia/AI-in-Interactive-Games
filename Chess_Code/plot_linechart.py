import matplotlib.pyplot as plt


x_axis = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
depth_2 = [0.484166538393, 0.452407426612, 0.476388519461,
           0.494060716629, 0.508375865313, 0.425787289182,
           0.500207945434, 0.468787180228, 0.464892190025,
           0.518313879848]
depth_3 = [5.81143887623, 8.0421860218, 5.46072000724,
           4.50419720411, 5.82801082004, 7.64024928353,
           5.73390220758, 4.27998794425, 8.44415667928,
           5.68857478703]
depth_4 = [27.1332941532, 73.1240674257, 39.321788366,
           51.4939635683, 40.3456965804, 26.1769292897,
           70.2881219672, 36.5946989477, 54.3586571985,
           38.6605024515]

dp2 = plt.plot(x_axis, depth_2, label='Depth 2')
plt.plot(x_axis, depth_3)
plt.plot(x_axis, depth_4)

plt.legend(['Depth 2', 'Depth 3', 'Depth 4'])

plt.ylabel('Avg. Time Taken')
plt.xlabel('Game No.')

plt.title('Average time taken for each depth')

plt.show()
