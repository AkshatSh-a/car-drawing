import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10,6))

ax.set_xlim(0,10)
ax.set_ylim(0,6)

sky = patches.Rectangle((0, 2), 10, 4, linewidth=0, facecolor= "skyblue")
ax.add_patch(sky)

ground = patches.Rectangle((0,0), 10, 2, linewidth=0, facecolor='green')
ax.add_patch(ground)

sun = patches.Circle((0,5), 0.8, linewidth = 2, edgecolor="orange", facecolor= "yellow")
ax.add_patch(sun)

mountain1 = patches.Polygon([[1, 2], [3, 5], [5, 2]], closed = True, linewidth= 2, edgecolor="brown", facecolor='darkgrey')
mountain2 = patches.Polygon([[4, 2], [6, 4.5], [8, 2]], closed = True, linewidth= 2, edgecolor="brown", facecolor='lightgrey')
mountain3 = patches.Polygon([[7, 2], [9, 4], [10, 2]], closed =True, linewidth= 2, edgecolor='brown', facecolor="darkgrey")

ax.add_patch(mountain1)
ax.add_patch(mountain2)
ax.add_patch(mountain3)

cloud1 = [patches.Circle((2, 5.5), 0.5, linewidth=0, facecolor = "white"),patches.Circle((2.5, 5.7), 0.7, linewidth= 0, facecolor= "white"),patches.Circle((3, 5.5), 0.5, linewidth= 0, facecolor=  "white"),]

cloud2 = [
    patches.Circle((6, 5.8), 0.5, linewidth = 0, facecolor= "white"),
    patches.Circle((6.5, 6), 0.7, linewidth = 0, facecolor= "white"),
    patches.Circle((7, 5.8), 0.5, linewidth = 0, facecolor = "white"),
]

for cloud in cloud1 + cloud2:
    ax.add_patch(cloud)

car_body = patches.Rectangle((2,2.2), 4, 1, linewidth= 2, edgecolor= "black", facecolor= "red")
ax.add_patch(car_body)

car_roof = patches.Rectangle((2,2.2),4,1, linewidth=2, edgecolor="black", facecolor='red')
ax.add_patch(car_roof)

window1 = patches.Polygon([[3.0, 3.2], [3.5, 3.6], [4.0, 3.6], [4.0, 3.2]], closed=True, linewidth = 1, edgecolor= 'black', facecolor= 'lightblue')
window2 = patches.Polygon([[4.0, 3.2], [4.5, 3.6], [5.0, 3.6], [5.0, 3.2]], closed=True, linewidth = 1, edgecolor= 'black', facecolor= 'lightblue')
ax.add_patch(window1)
ax.add_patch(window2)

wheel1 = patches.Circle((3,2.2), 0.5, linewidth = 2, edgecolor="black", facecolor="gray")
wheel2 = patches.Circle((5,2.2), 0.5, linewidth = 2, edgecolor="black", facecolor="gray")
ax.add_patch(wheel1)
ax.add_patch(wheel2)

tree_trunk = patches.Rectangle((7, 2), 0.3, 1.5, linewidth = 1, edgecolor="brown", facecolor = "brown")
tree_leaves = patches.Circle((7.15, 3.7), 1, linewidth= 2, edgecolor= "green", facecolor="green")
ax.add_patch(tree_trunk)
ax.add_patch(tree_leaves)

ax.set_aspect("equal")
ax.axis("off")

plt.show()