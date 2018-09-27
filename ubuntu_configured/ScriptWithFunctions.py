def vlans_exist(vlansID):
	VlansList = [1, 10, 20, 30]
	return vlansID in VlansList

if __name__ == "__main__":

	vlan = [1, 20, 100, 200]
	for Vlan in vlan:
		print Vlan, vlans_exist(Vlan)
		