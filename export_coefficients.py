# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Default export coefficients based on KUSTAA Excel-tool
"""
default_coeff = {
    'NATURAL': {
        'Background': {'N': [1.25, 0.29, 2.30], 'P': [0.049, 0.018, 0.146], 'SS': [5.1, 0.9, 47.0]},	# kg/ha/a
        'Deposition': {'N': [3.0, 2.0, 4.0], 'P':	[0.10, 0.07, 0.15], 'SS': [0.0, 0.0, 0.0]},
		},
	'FORESTRY': { # kg/ha/10 a
		'Renewal_upland': {'N': [5.0, 0.0, 10.0], 'P': [0.3, 0.00, 0.8], 'SS': [0.0, 0.0, 0.0]},
		'Renewal_peatland': {'N': [26.0, 12.0, 40.0], 'P': [0.6, 0.3, 0.9], 'SS': [0.0, 0.0, 0.0]},
		'Ditching': {'N': [23.0, 12.0, 34.0], 'P': [1.7, 0.00, 3.9], 'SS': [2460.0,	170.0,	8550.0]},
		'Ditch_maintenance': {'N': [0.0, 0.0, 0.0], 'P': [1.0, 0.00, 2.2], 'SS': [970.0, 500.0, 1500.0]},
		'Fertilization_upland': {'N': [15.0, 0.0, 30.0], 'P': [0.00, 0.00, 0.00], 'SS': [0.0, 0.0, 0.0]},
		'Fertilization_peatland': {'N': [0, 0, 0], 'P': [1.4,	0.00, 2.8], 'SS': [0.0, 0.0, 0.0]}
		},
			
	'PEATEXTRACTION': {	# kg/ha/a
		'Establishment_pintavalutus': {'N': [7.8, 0.0, 17.6], 'P': [0.23, 0.00, 0.46], 'SS': [17.0, 0.0, 34.0]},
		'Establishment_basic': {'N': [10.1, 0.0, 20.2], 'P': [0.41, 0.00, 0.82], 'SS': [74, 0.0, 148]},
		'Baselevel': {'N': [8.6, 0.0, 17.2], 'P': [0.30, 0.00, 0.60], 'SS': [53.0, 0.0, 106.0]},
		'Flowcontrol': {'N': [9.1, 0.0, 11.4], 'P': [0.22, 0.00, 0.44], 'SS': [42.0, 0.0, 84.0]},
		'Vegetation': {'N': [5.7, 0.0, 11.4], 'P': [0.27, 0.00, 0.54], 'SS': [24.0, 0.0, 48.0]},
		'Pintavalutus_summer': {'N': [5.7, 0.0, 11.4], 'P': [0.24, 0.00, 0.48], 'SS': [35.0, 0.0, 70.0]},
		'Pintavalutus': {'N': [4.6, 0.0, 9.2], 'P':	[0.11, 0.00, 0.22], 'SS': [11, 0.0, 22]},
		'Chemicals': {'N': [6.4, 0.0, 12.8], 'P': [0.22, 0.00, 0.44], 'SS':	[48.0, 0.0, 96.0]}
		},

	'AGRICULTURE': { # kg/ha/a
		'Syyskynto': {'N': [17.9, 15.0, 20.0], 'P': [1.14, 0.84, 1.64], 'SS': [925.0, 720.0, 1090.0]},
		'Syysvilja': {'N': [21.4, 17.2, 21.4], 'P': [0.93, 0.67, 1.26], 'SS': [690.0, 540.0, 815.0]},
		'Kultivointi': {'N': [11.9, 10.6, 12.7], 'P': [1.06, 0.76, 1.48], 'SS': [775.0, 605.0, 910.0]},
		'Sankimuokkaus': {'N': [9.9, 5.1, 15.5], 'P': [0.95, 0.64, 1.43], 'SS': [625.0, 485.0, 735.0]},
		'Sanki': {'N': [12.1, 9.3, 14.3], 'P': [1.03, 0.67, 1.49], 'SS':[605.0, 470.0, 710.0]},
		'Suorakylvo_syysvilja': {'N': [9.9, 9.0, 11.1], 'P': [1.59, 0.99, 2.67], 'SS': [330.0, 290.0, 355.0]},
		'Suorakylvo_kevatvilja': {'N': [9.9, 9.0, 11.1], 'P': [1.21, 0.80, 1.77], 'SS':[330.0, 290.0, 355.0]},
		'Permanent_grass': {'N': [7.2, 5.2, 8.2],	'P': [1.00, 0.70, 1.43], 'SS': [305.0, 290.0, 320.0]},
		'Viherkesanto': {'N': [7.2, 5.2, 8.2],	'P': [1.13, 0.80, 1.50], 'SS': [305.0, 290.0, 320.0]},
		'Avokesanto': {'N': [17.9, 15.0, 20.0], 'P': [1.29,	0.90, 1.80], 'SS': [925.0, 720.0, 1090.0]}
		},
									
	'LIVESTOCK': { # kg/animal/a
		'Poultry': {'N': [0.013, None, None], 'P':	[0.002, None, None], 'SS': [0.0, None, None]},
		'Cow': {'N': [2.5, None, None], 'P':	[0.44, None, None], 'SS': [0.0, None, None]},
		'Cattle': {'N': [1.3, None, None], 'P':	[0.22, None, None], 'SS': [0.0, None, None]},
		'Swine': {'N': [0.4, None, None], 'P':	[0.07, None, None], 'SS': [0.0, None, None]},
		'Reindeer': {'N': [0.4, None, None], 'P':	[0.06, None, None], 'SS': [0.0, None, None]}
		},
			
	'COMMUNITY': {						
		'Urban_household': {'N': [2.4, 0.6, 4.4], 'P': [0.03, 0.01, 0.18], 'SS': [0.4, 0.003, 0.884]},	#
		'Scattered_household': {'N': [1.0, None, None], 'P': [0.25, None, None], 'SS': [3.7, None, None]},
		'Scattered_household_requirement': {'N': [3.6, None, None], 'P': [0.24, None, None], 'SS': [3.7, None, None]},
		'Cottages': {'N': [0.4, 0.1, 1.1], 'P': [0.07, 0.01, 0.19], 'SS': [3.7, 0.003, 10.076]}, 
		'Urban_runoff': {'N': [5.6, 2.9, 8.8], 'P': [0.66, 0.24, 1.36], 'SS': [372, 110, 790]} 
		},
																					
	'INDUSTRY': {
		'Pulp': {'N': [0.18, 0.01, 0.45], 'P': [0.015, 0.007, 0.040], 'SS': [0.6, 0.0, 2.6]},			# kg/ton
		'Paper': {'N': [0.14, 0.03, 0.31], 'P': [0.008, 0.003, 0.017], 'SS': [0.4, 0.1, 0.7]},			# kg/ton
		'Fishfarming_land': {'N': [39.0, None, None], 'P': [7.2, None, None], 'SS': [0.0, 0.0, 0.0]},	# kg/ton
		'Fishfarming': {'N': [44.0, None, None], 'P': [7.0, None, None], 'SS': [0.0, 0.0, 0.0]},		# kg/ton
		'Furfarming': {'N': [253.0, None, None], 'P': [26.5, None, None], 'SS': [0.0, 0.0, 0.0]}		# kg/farm/a
		}
    }


"""
relative export coefficients from forestry operations during the 10-year period
"""  
forestry_relative = {
        'Renewal_upland': {'N': [0.189, 0.163, 0.163, 0.153, 0.123, 0.070, 0.066, 0.040, 0.032, 0.001],
                            'P': [0.223, 0.175, 0.147, 0.151, 0.096, 0.044, 0.052, 0.052, 0.036, 0.024], 
                            'SS': [0.0]
                            },
         'Renewal_peatland': {'N': [0.166, 0.166, 0.166, 0.143, 0.119, 0.095, 0.072, 0.049, 0.024, 0.001],
                              'P': [0.157, 0.157, 0.157, 0.136, 0.116, 0.096, 0.076, 0.055, 0.035, 0.015],
                              'SS': [0.0]
                              },
         'Ditching': {'N': [0.051, 0.103, 0.132, 0.230, 0.183, 0.118, 0.088, 0.023, 0.049, 0.032],
                      'P': [0.100, 0.192, 0.118, 0.158, 0.144, 0.156, 0.058, 0.020, 0.024, 0.032],
                      'SS': [0.085, 0.364, 0.134, 0.187, 0.042, 0.069, 0.0514, 0.0595, 0.0, 0.008]
                      },
         'Ditch_maintenance': {'N': [0.0],
                               'P': [0.432, 0.144, 0.115, 0.086, 0.072, 0.058, 0.043, 0.029, 0.014, 0.007],
                               'SS': [0.432, 0.144, 0.115, 0.086, 0.072, 0.058, 0.043, 0.029, 0.014, 0.007]
                               },
         'Fertilization_upland': {'N': [0.8, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                  'P': [0.0],
                                  'SS': [0.0]
                                  },
         'Fertilization_peatland': {'N': [0.0],
                                  'P': [0.2, 0.2, 0.2, 0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0],
                                  'SS': [0.0]
                                  }         
        }



    
    
