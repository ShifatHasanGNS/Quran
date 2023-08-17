import json
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon


# On the X-axis: for Surah number n, x = 114 - n
def V(surah_numbers: list[int]) -> list:
    v = []
    for n in surah_numbers:
        x: int = 114 - n
        y: int = ayahs_count[x]
        v.append((x, y))
    return v


# Load Data

with open('surahs.json', 'r') as json_file:
    surahs = json.load(json_file)

names = []
ayahs_count = []

for i in range(114, 0, -1):
    order = str(i)
    name = surahs[order]['name_simple']
    ayah_count = surahs[order]['ayah_count']
    names.append(name)
    ayahs_count.append(ayah_count)


# Plot

polygon1 = Polygon(
    # [(x, y), ...]
    V([1, 2, 7, 6, 5]),
    color='skyblue', alpha=0.75, closed=True
)

polygon2 = Polygon(
    # [(x, y), ...]
    V([8, 9, 26, 20, 23, 27, 28, 37, 43, 51, 53, 55, 56, 68, 69, 74, 114, 113,
      112, 110, 108, 103, 97, 73, 66, 65, 63, 62, 61, 60, 49, 45, 41, 32, 13]),
    color='skyblue', alpha=0.75, closed=True
)

fig, ax = plt.subplots()

ax.add_patch(polygon1)
ax.add_patch(polygon2)

plt.ylim(-10, 310)
plt.xlim(-1, 115)

plt.title('Ayah-Count of each Surah', fontsize=12, fontweight='bold',
          fontname='Times New Roman', color='black', verticalalignment='baseline')

plt.xlabel('Surah-Name', fontsize=10, fontname='Times New Roman',
           fontweight='bold', color='black')
plt.ylabel('Ayah-Count', fontsize=10, fontname='Times New Roman',
           fontweight='bold', color='black')

plt.xticks(rotation=90, fontsize=3, fontname='Times New Roman',
           fontweight='bold', color='black', label='Surah-Name')
plt.yticks(range(0, 310, 10), fontsize=3, fontname='Times New Roman',
           fontweight='bold', color='black', label='Ayah-Count')

plt.scatter(names, ayahs_count, s=1, c='red', marker='.', alpha=1)
plt.plot(names, ayahs_count, '-', c='black', alpha=0.05)
plt.plot(names[46:49], ayahs_count[46:49], '-', c='black', alpha=0.1)

plt.savefig('plot.png', bbox_inches='tight', dpi=1024)
