import numpy as np

# Returns the preferance matrix
def generate_prefmatrix():
# 		Forrest_Gump | Frozen | Star_Wars | Parent_Trap | The_Notebook | Harry_Potter | Bat_Man | Finding_Nemo | The_Hangover | Inception
	return np.array([
		[1,				0,		0,			1,				1,			0,				0,			0,			0,				0], #Drama
		[0,				1,		0,			0,				1,			1,				0,			1,			0,				0], #Family
		[0,				0,		1,			0,				0,			1,				1,			1,			0,				1], #Adventure
		[1,				0,		0,			1,				0,			0,				0,			1,			1,				0], #Comedy
		[1,				0,		0,			1,				1,			0,				0,			0,			0,				0], #Romance
		[0,				0,		1,			0,				0,			1,				0,			0,			0,				0], #Fantasy/Sci-Fi
		[0,				0,		1,			0,				0,			1,				1,			0,			0,				1], #Action
		[0,				0,		0,			0,				0,			1,				0,			0,			0,				1], #Mystery
		[0,				1,		1,			0				0,			1,				1,			0,			0,				0], #Political
		[0,				1,		0,			0,				0,			0,				0,			1,			0,				0]  #Animation
		])
		