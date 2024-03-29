#   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#   !                                                                           !
#   ! Copyright 2021 by Tyler C. Sterling and Dmitry Reznik,                    !
#   ! University of Colorado Boulder                                            !
#   !                                                                           !
#   ! This file is part of the pynamic-structure-factor (PSF) software.         !
#   ! PSF is free software: you can redistribute it and/or modify it under      !
#   ! the terms of the GNU General Public License as published by the           !
#   ! Free software Foundation, either version 3 of the License, or             !
#   ! (at your option) any later version. PSF is distributed in the hope        !
#   ! that it will be useful, but WITHOUT ANY WARRANTY; without even the        !
#   ! implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  !
#   ! See the GNU General Public License for more details.                      !
#   !                                                                           !
#   ! A copy of the GNU General Public License should be available              !
#   ! alongside this source in a file named gpl-3.0.txt. If not see             !
#   ! <http://www.gnu.org/licenses/>.                                           !
#   !                                                                           !
#   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""
these are from the NIST database at: https://www.nist.gov/ncnr/neutron-scattering-lengths-list
which are from Neutron News, Vol. 3, No. 3, 1992, pp. 29-37. 

the given value is 'coherent_b' in femtometers
"""

scattering_lengths = { \
        'none'   :       0.000000+0.000000j, 
        'H'      :      -3.739000+0.000000j, 
        '1H'     :      -3.740600+0.000000j, 
        '2H'     :       6.671000+0.000000j, 
        '3H'     :       4.792000+0.000000j, 
        'He'     :       3.260000+0.000000j, 
        '3He'    :       5.740000-1.483000j, 
        '4He'    :       3.260000+0.000000j, 
        'Li'     :      -1.900000+0.000000j, 
        '6Li'    :       2.000000-0.261000j, 
        '7Li'    :      -2.220000+0.000000j, 
        'Be'     :       7.790000+0.000000j, 
        'B'      :       5.300000-0.213000j, 
        '10B'    :      -0.100000-1.066000j, 
        '11B'    :       6.650000+0.000000j, 
        'C'      :       6.646000+0.000000j, 
        '12C'    :       6.651100+0.000000j, 
        '13C'    :       6.190000+0.000000j, 
        'N'      :       9.360000+0.000000j, 
        '14N'    :       9.370000+0.000000j, 
        '15N'    :       6.440000+0.000000j, 
        'O'      :       5.803000+0.000000j, 
        '16O'    :       5.803000+0.000000j, 
        '17O'    :       5.780000+0.000000j, 
        '18O'    :       5.840000+0.000000j, 
        'F'      :       5.654000+0.000000j, 
        'Ne'     :       4.566000+0.000000j, 
        '20Ne'   :       4.631000+0.000000j, 
        '21Ne'   :       6.660000+0.000000j, 
        '22Ne'   :       3.870000+0.000000j, 
        'Na'     :       3.630000+0.000000j, 
        'Mg'     :       5.375000+0.000000j, 
        '24Mg'   :       5.660000+0.000000j, 
        '25Mg'   :       3.620000+0.000000j, 
        '26Mg'   :       4.890000+0.000000j, 
        'Al'     :       3.449000+0.000000j, 
        'Si'     :       4.149100+0.000000j, 
        '28Si'   :       4.107000+0.000000j, 
        '29Si'   :       4.700000+0.000000j, 
        '30Si'   :       4.580000+0.000000j, 
        'P'      :       5.130000+0.000000j, 
        'S'      :       2.847000+0.000000j, 
        '32S'    :       2.804000+0.000000j, 
        '33S'    :       4.740000+0.000000j, 
        '34S'    :       3.480000+0.000000j, 
        '36S'    :       3.000000+0.000000j, 
        'Cl'     :       9.577000+0.000000j, 
        '35Cl'   :      11.650000+0.000000j, 
        '37Cl'   :       3.080000+0.000000j, 
        'Ar'     :       1.909000+0.000000j, 
        '36Ar'   :      24.900000+0.000000j, 
        '38Ar'   :       3.500000+0.000000j, 
        '40Ar'   :       1.830000+0.000000j, 
        'K'      :       3.670000+0.000000j, 
        '39K'    :       3.740000+0.000000j, 
        '40K'    :       3.000000+0.000000j, 
        '41K'    :       2.690000+0.000000j, 
        'Ca'     :       4.700000+0.000000j, 
        '40Ca'   :       4.800000+0.000000j, 
        '42Ca'   :       3.360000+0.000000j, 
        '43Ca'   :      -1.560000+0.000000j, 
        '44Ca'   :       1.420000+0.000000j, 
        '46Ca'   :       3.600000+0.000000j, 
        '48Ca'   :       0.390000+0.000000j, 
        'Sc'     :      12.290000+0.000000j, 
        'Ti'     :      -3.438000+0.000000j, 
        '46Ti'   :       4.930000+0.000000j, 
        '47Ti'   :       3.630000+0.000000j, 
        '48Ti'   :      -6.080000+0.000000j, 
        '49Ti'   :       1.040000+0.000000j, 
        '50Ti'   :       6.180000+0.000000j, 
        'V'      :      -0.382400+0.000000j, 
        '50V'    :       7.600000+0.000000j, 
        '51V'    :      -0.402000+0.000000j, 
        'Cr'     :       3.635000+0.000000j, 
        '50Cr'   :      -4.500000+0.000000j, 
        '52Cr'   :       4.920000+0.000000j, 
        '53Cr'   :      -4.200000+0.000000j, 
        '54Cr'   :       4.550000+0.000000j, 
        'Mn'     :      -3.730000+0.000000j, 
        'Fe'     :       9.450000+0.000000j, 
        '54Fe'   :       4.200000+0.000000j, 
        '56Fe'   :       9.940000+0.000000j, 
        '57Fe'   :       2.300000+0.000000j, 
        '58Fe'   :      15.000000+0.000000j, 
        'Co'     :       2.490000+0.000000j, 
        'Ni'     :      10.300000+0.000000j, 
        '58Ni'   :      14.400000+0.000000j, 
        '60Ni'   :       2.800000+0.000000j, 
        '61Ni'   :       7.600000+0.000000j, 
        '62Ni'   :      -8.700000+0.000000j, 
        '64Ni'   :      -0.370000+0.000000j, 
        'Cu'     :       7.718000+0.000000j, 
        '63Cu'   :       6.430000+0.000000j, 
        '65Cu'   :      10.610000+0.000000j, 
        'Zn'     :       5.680000+0.000000j, 
        '64Zn'   :       5.220000+0.000000j, 
        '66Zn'   :       5.970000+0.000000j, 
        '67Zn'   :       7.560000+0.000000j, 
        '68Zn'   :       6.030000+0.000000j, 
        '70Zn'   :       6.000000+0.000000j, 
        'Ga'     :       7.288000+0.000000j, 
        '69Ga'   :       7.880000+0.000000j, 
        '71Ga'   :       6.400000+0.000000j, 
        'Ge'     :       8.185000+0.000000j, 
        '70Ge'   :      10.000000+0.000000j, 
        '72Ge'   :       8.510000+0.000000j, 
        '73Ge'   :       5.020000+0.000000j, 
        '74Ge'   :       7.580000+0.000000j, 
        '76Ge'   :       8.200000+0.000000j, 
        'As'     :       6.580000+0.000000j, 
        'Se'     :       7.970000+0.000000j, 
        '74Se'   :       0.800000+0.000000j, 
        '76Se'   :      12.200000+0.000000j, 
        '77Se'   :       8.250000+0.000000j, 
        '78Se'   :       8.240000+0.000000j, 
        '80Se'   :       7.480000+0.000000j, 
        '82Se'   :       6.340000+0.000000j, 
        'Br'     :       6.795000+0.000000j, 
        '79Br'   :       6.800000+0.000000j, 
        '81Br'   :       6.790000+0.000000j, 
        'Kr'     :       7.810000+0.000000j, 
        '86Kr'   :       8.100000+0.000000j, 
        'Rb'     :       7.090000+0.000000j, 
        '85Rb'   :       7.030000+0.000000j, 
        '87Rb'   :       7.230000+0.000000j, 
        'Sr'     :       7.020000+0.000000j, 
        '84Sr'   :       7.000000+0.000000j, 
        '86Sr'   :       5.670000+0.000000j, 
        '87Sr'   :       7.400000+0.000000j, 
        '88Sr'   :       7.150000+0.000000j, 
        'Y'      :       7.750000+0.000000j, 
        'Zr'     :       7.160000+0.000000j, 
        '90Zr'   :       6.400000+0.000000j, 
        '91Zr'   :       8.700000+0.000000j, 
        '92Zr'   :       7.400000+0.000000j, 
        '94Zr'   :       8.200000+0.000000j, 
        '96Zr'   :       5.500000+0.000000j, 
        'Nb'     :       7.054000+0.000000j, 
        'Mo'     :       6.715000+0.000000j, 
        '92Mo'   :       6.910000+0.000000j, 
        '94Mo'   :       6.800000+0.000000j, 
        '95Mo'   :       6.910000+0.000000j, 
        '96Mo'   :       6.200000+0.000000j, 
        '97Mo'   :       7.240000+0.000000j, 
        '98Mo'   :       6.580000+0.000000j, 
        '100Mo'  :       6.730000+0.000000j, 
        'Tc'     :       6.800000+0.000000j, 
        'Ru'     :       7.030000+0.000000j, 
        'Rh'     :       5.880000+0.000000j, 
        'Pd'     :       5.910000+0.000000j, 
        '102Pd'  :       7.700000+0.000000j, 
        '104Pd'  :       7.700000+0.000000j, 
        '105Pd'  :       5.500000+0.000000j, 
        '106Pd'  :       6.400000+0.000000j, 
        '108Pd'  :       4.100000+0.000000j, 
        '110Pd'  :       7.700000+0.000000j, 
        'Ag'     :       5.922000+0.000000j, 
        '107Ag'  :       7.555000+0.000000j, 
        '109Ag'  :       4.165000+0.000000j, 
        'Cd'     :       4.870000-0.700000j, 
        '106Cd'  :       5.000000+0.000000j, 
        '108Cd'  :       5.400000+0.000000j, 
        '110Cd'  :       5.900000+0.000000j, 
        '111Cd'  :       6.500000+0.000000j, 
        '112Cd'  :       6.400000+0.000000j, 
        '113Cd'  :      -8.000000-5.730000j, 
        '114Cd'  :       7.500000+0.000000j, 
        '116Cd'  :       6.300000+0.000000j, 
        'In'     :       4.065000-0.053900j, 
        '113In'  :       5.390000+0.000000j, 
        '115In'  :       4.010000-0.056200j, 
        'Sn'     :       6.225000+0.000000j, 
        '112Sn'  :       6.000000+0.000000j, 
        '114Sn'  :       6.200000+0.000000j, 
        '115Sn'  :       6.000000+0.000000j, 
        '116Sn'  :       5.930000+0.000000j, 
        '117Sn'  :       6.480000+0.000000j, 
        '118Sn'  :       6.070000+0.000000j, 
        '119Sn'  :       6.120000+0.000000j, 
        '120Sn'  :       6.490000+0.000000j, 
        '122Sn'  :       5.740000+0.000000j, 
        '124Sn'  :       5.970000+0.000000j, 
        'Sb'     :       5.570000+0.000000j, 
        '121Sb'  :       5.710000+0.000000j, 
        '123Sb'  :       5.380000+0.000000j, 
        'Te'     :       5.800000+0.000000j, 
        '120Te'  :       5.300000+0.000000j, 
        '122Te'  :       3.800000+0.000000j, 
        '123Te'  :      -0.050000-0.116000j, 
        '124Te'  :       7.960000+0.000000j, 
        '125Te'  :       5.020000+0.000000j, 
        '126Te'  :       5.560000+0.000000j, 
        '128Te'  :       5.890000+0.000000j, 
        '130Te'  :       6.020000+0.000000j, 
        'I'      :       5.280000+0.000000j, 
        'Xe'     :       4.920000+0.000000j, 
        'Cs'     :       5.420000+0.000000j, 
        'Ba'     :       5.070000+0.000000j, 
        '130Ba'  :      -3.600000+0.000000j, 
        '132Ba'  :       7.800000+0.000000j, 
        '134Ba'  :       5.700000+0.000000j, 
        '135Ba'  :       4.670000+0.000000j, 
        '136Ba'  :       4.910000+0.000000j, 
        '137Ba'  :       6.830000+0.000000j, 
        '138Ba'  :       4.840000+0.000000j, 
        'La'     :       8.240000+0.000000j, 
        '138La'  :       8.000000+0.000000j, 
        '139La'  :       8.240000+0.000000j, 
        'Ce'     :       4.840000+0.000000j, 
        '136Ce'  :       5.800000+0.000000j, 
        '138Ce'  :       6.700000+0.000000j, 
        '140Ce'  :       4.840000+0.000000j, 
        '142Ce'  :       4.750000+0.000000j, 
        'Pr'     :       4.580000+0.000000j, 
        'Nd'     :       7.690000+0.000000j, 
        '142Nd'  :       7.700000+0.000000j, 
        '143Nd'  :      14.000000+0.000000j, 
        '144Nd'  :       2.800000+0.000000j, 
        '145Nd'  :      14.000000+0.000000j, 
        '146Nd'  :       8.700000+0.000000j, 
        '148Nd'  :       5.700000+0.000000j, 
        '150Nd'  :       5.300000+0.000000j, 
        'Pm'     :      12.600000+0.000000j, 
        'Sm'     :       0.800000-1.650000j, 
        '144Sm'  :      -3.000000+0.000000j, 
        '147Sm'  :      14.000000+0.000000j, 
        '148Sm'  :      -3.000000+0.000000j, 
        '149Sm'  :    -19.200000-11.700000j, 
        '150Sm'  :      14.000000+0.000000j, 
        '152Sm'  :      -5.000000+0.000000j, 
        '154Sm'  :       9.300000+0.000000j, 
        'Eu'     :       7.220000-1.260000j, 
        '151Eu'  :       6.130000-2.530000j, 
        '153Eu'  :       8.220000+0.000000j, 
        'Gd'     :      6.500000-13.820000j, 
        '152Gd'  :      10.000000+0.000000j, 
        '154Gd'  :      10.000000+0.000000j, 
        '155Gd'  :      6.000000-17.000000j, 
        '156Gd'  :       6.300000+0.000000j, 
        '157Gd'  :     -1.140000-71.900000j, 
        '158Gd'  :       9.000000+0.000000j, 
        '160Gd'  :       9.150000+0.000000j, 
        'Tb'     :       7.380000+0.000000j, 
        'Dy'     :      16.900000-0.276000j, 
        '156Dy'  :       6.100000+0.000000j, 
        '158Dy'  :       6.000000+0.000000j, 
        '160Dy'  :       6.700000+0.000000j, 
        '161Dy'  :      10.300000+0.000000j, 
        '162Dy'  :      -1.400000+0.000000j, 
        '163Dy'  :       5.000000+0.000000j, 
        '164Dy'  :      49.400000-0.790000j, 
        'Ho'     :       8.010000+0.000000j, 
        'Er'     :       7.790000+0.000000j, 
        '162Er'  :       8.800000+0.000000j, 
        '164Er'  :       8.200000+0.000000j, 
        '166Er'  :      10.600000+0.000000j, 
        '167Er'  :       3.000000+0.000000j, 
        '168Er'  :       7.400000+0.000000j, 
        '170Er'  :       9.600000+0.000000j, 
        'Tm'     :       7.070000+0.000000j, 
        'Yb'     :      12.430000+0.000000j, 
        '168Yb'  :      -4.070000-0.620000j, 
        '170Yb'  :       6.770000+0.000000j, 
        '171Yb'  :       9.660000+0.000000j, 
        '172Yb'  :       9.430000+0.000000j, 
        '173Yb'  :       9.560000+0.000000j, 
        '174Yb'  :      19.300000+0.000000j, 
        '176Yb'  :       8.720000+0.000000j, 
        'Lu'     :       7.210000+0.000000j, 
        '175Lu'  :       7.240000+0.000000j, 
        '176Lu'  :       6.100000-0.570000j, 
        'Hf'     :       7.700000+0.000000j, 
        '174Hf'  :      10.900000+0.000000j, 
        '176Hf'  :       6.610000+0.000000j, 
        '177Hf'  :       0.800000+0.000000j, 
        '178Hf'  :       5.900000+0.000000j, 
        '179Hf'  :       7.460000+0.000000j, 
        '180Hf'  :      13.200000+0.000000j, 
        'Ta'     :       6.910000+0.000000j, 
        '180Ta'  :       7.000000+0.000000j, 
        '181Ta'  :       6.910000+0.000000j, 
        'W'      :       4.860000+0.000000j, 
        '180W'   :       5.000000+0.000000j, 
        '182W'   :       6.970000+0.000000j, 
        '183W'   :       6.530000+0.000000j, 
        '184W'   :       7.480000+0.000000j, 
        '186W'   :      -0.720000+0.000000j, 
        'Re'     :       9.200000+0.000000j, 
        '185Re'  :       9.000000+0.000000j, 
        '187Re'  :       9.300000+0.000000j, 
        'Os'     :      10.700000+0.000000j, 
        '184Os'  :      10.000000+0.000000j, 
        '186Os'  :      11.600000+0.000000j, 
        '187Os'  :      10.000000+0.000000j, 
        '188Os'  :       7.600000+0.000000j, 
        '189Os'  :      10.700000+0.000000j, 
        '190Os'  :      11.000000+0.000000j, 
        '192Os'  :      11.500000+0.000000j, 
        'Ir'     :      10.600000+0.000000j, 
        'Pt'     :       9.600000+0.000000j, 
        '190Pt'  :       9.000000+0.000000j, 
        '192Pt'  :       9.900000+0.000000j, 
        '194Pt'  :      10.550000+0.000000j, 
        '195Pt'  :       8.830000+0.000000j, 
        '196Pt'  :       9.890000+0.000000j, 
        '198Pt'  :       7.800000+0.000000j, 
        'Au'     :       7.630000+0.000000j, 
        'Hg'     :      12.692000+0.000000j, 
        '196Hg'  :      30.300000+0.000000j, 
        '199Hg'  :      16.900000+0.000000j, 
        'Tl'     :       8.776000+0.000000j, 
        '203Tl'  :       6.990000+0.000000j, 
        '205Tl'  :       9.520000+0.000000j, 
        'Pb'     :       9.405000+0.000000j, 
        '204Pb'  :       9.900000+0.000000j, 
        '206Pb'  :       9.220000+0.000000j, 
        '207Pb'  :       9.280000+0.000000j, 
        '208Pb'  :       9.500000+0.000000j, 
        'Bi'     :       8.532000+0.000000j, 
        'Ra'     :      10.000000+0.000000j, 
        'Th'     :      10.310000+0.000000j, 
        'Pa'     :       9.100000+0.000000j, 
        'U'      :       8.417000+0.000000j, 
        '233U'   :      10.100000+0.000000j, 
        '234U'   :      12.400000+0.000000j, 
        '235U'   :      10.470000+0.000000j, 
        '238U'   :       8.402000+0.000000j, 
        'Np'     :      10.550000+0.000000j, 
        '238Pu'  :      14.100000+0.000000j, 
        '239Pu'  :       7.700000+0.000000j, 
        '240Pu'  :       3.500000+0.000000j, 
        '242Pu'  :       8.100000+0.000000j, 
        'Am'     :       8.300000+0.000000j, 
        '244Cm'  :       9.500000+0.000000j, 
        '246Cm'  :       9.300000+0.000000j, 
        '248Cm'  :       7.700000+0.000000j}
