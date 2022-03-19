import sys
import matplotlib.pyplot as plt

energy = sys.argv[1]
energy_bin = sys.argv[2]
particle = sys.argv[3]
exec('count_list = [' + sys.argv[4] + ']')
mode = sys.argv[5]
dir = sys.argv[6]

energy_list = list(range(0, energy, energy_bin))
total_count = sum(count_list)

plt.figure(figsize = (10,5), dpi = 72)
plt.text(0, max(count_list), 'Total Number of ' + particle + ': ' + str(total_count))
plt.bar(energy_list, count_list, width = energy_bin)
plt.title(particle + 'energy spectrum')
plt.xlabel('Energy(MeV)')
plt.ylabel('Count')
plt.yscale(mode)

figure_name = dir + '/' + particle + '_energy_spectrum_' + mode + '.png'
plt.savefig(figure_name)
os.system('viu ' + figure_name)
