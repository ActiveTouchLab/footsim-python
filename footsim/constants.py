import numpy as np


def epiThick(loc):

    """ Computes the skin thickness of a given foot sole region.

          Arguments:

              region(str): Region of interest.

           Returns:

              Skin thickness value in arbitrary units retrieved from the literature.

           """

    if (loc == 'T1'):
        return 1.07

    if ((loc == 'T2_t') or (loc == 'T3_t') or (loc == 'T4_t') or (loc == 'T5_t')):
        return 0.6

    if (loc == 'MMi'):
        return 1.21

    if (loc == 'MMe'):
        return 1.21

    if (loc == 'MLa'):
        return 1.21

    if (loc == 'AMe'):
        return 0.76

    if (loc == 'AMi'):
        return 0.8

    if (loc == 'ALa'):
        return 0.92

    if ((loc == 'HL') or (loc == 'HR')):

        return 1.32

    else:

        return 0


def hardnessRegion(region):

    """ Computes the hardness of each foot sole region.

        Arguments:

            region(str): Region of interest.

         Returns:

            Hardness value in arbitrary units retrieved from the literature.

         """

    if(region=='T1'):
        return 48.13

    if((region=='T2_t') or (region=='T3_t') or (region=='T4_t') or (region=='T5_t')):
        return 34.93

    if(region=='MMi'):
        return 30.27

    if(region=='MMe'):
        return 26.235

    if(region=='MLa'):
        return 31.229

    if(region=='AMe'):
        return 25.24

    if(region=='AMi'):
        return 31.06

    if(region=='ALa'):
        return 34.366

    if((region=='HL')or(region=='HR')):
        return 40.91


affclasses = ['SA1','FA1','FA2','SA2']
affclass_mapping = {'SA1':'SA1','SA':'SA1','SAI':'SA1',
                    'FA1':'FA1','FAI':'FA1','RA':'FA1','RA1':'FA1',
                    'FA2':'FA2','PC':'FA2','FAII':'FA2',
                    'SA2':'SA2','SAII':'SA2',}

# Afferent depths in skin
affdepths = {'SA1':0.3,'FA1':1.6,'FA2':2.,'SA2':1.}

# SA1 parameters
affparamsSA1 = np.array([[ 2.80703655e+00,  8.17434305e-01, -3.23256841e-01,
         8.12509293e-02, -1.13041290e-01,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         9.93965989e+02, -7.38359949e-02, -9.94032155e-01,
         0.00000000e+00],
       [ 1.01301261e+01,  9.98945035e-01, -2.24771308e-01,
         1.19367275e-06,  2.13393816e-05,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         1.48982674e+02, -1.13564554e-01, -5.75095770e-03,
         0.00000000e+00],
       [ 8.84883112e+00,  5.71708347e-01,  4.57890635e-01,
         4.67882736e-05,  4.44155182e-05,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         9.29404047e+02, -7.49234861e-02, -2.38258912e-03,
         0.00000000e+00],
       [ 1.07097416e+01,  3.92620246e-01, -3.90669408e-02,
         8.98857098e-05, -5.55111052e-05,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         1.99157511e+02, -5.55032574e-01, -2.03891958e-02,
         0.00000000e+00],
       [ 7.54061099e+00,  9.02520117e-01,  8.87938370e-01,
         3.30692638e-03, -3.28318230e-03,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         1.92384635e+02, -5.16704014e-01, -7.07843894e-04,
         0.00000000e+00]])

# SA2 parameters
affparamsSA2 = np.array([[ 9.80080199e+00,  9.98128400e-01, -7.88832241e-01,
         3.35644720e-04,  5.36704683e-04,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         1.18485356e+02, -2.15497784e-01, -1.09556697e-02,
         0.00000000e+00],
       [ 4.98378790e+00,  8.79132612e-01,  9.15460405e-01,
         6.01878073e-03, -1.55199961e-03,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         9.39491683e+02, -1.96974386e-02, -1.68921219e-01,
         0.00000000e+00],
       [ 7.94347874e+00,  7.93109781e-01,  7.73778476e-01,
         1.66249550e-02, -1.07211490e-02,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         9.40980351e+02, -1.81717699e-01, -4.15879176e-01,
         0.00000000e+00],
       [ 2.40466199e+00,  9.97449147e-01, -9.36084312e-01,
         8.20808637e-04, -9.17632339e-04,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         1.64594821e+02, -9.14630506e-02, -7.47781267e-04,
         0.00000000e+00],
       [ 8.20650980e+00,  8.55033176e-01,  9.39502378e-01,
         4.97634072e-02, -3.90350261e-02,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         4.76912847e+02, -4.19914964e-01, -8.78754915e-01,
         0.00000000e+00],
       [ 6.62570984e+00,  9.12810637e-01, -2.62955285e-01,
         4.16895995e-03,  5.68165681e-04,  0.00000000e+00,
         0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
         2.05459909e+02, -5.43557079e-03, -3.77347321e-01,
         0.00000000e+00]])

# RA parameters
affparamsFA1 = np.array([[ 8.61614226e+00,  0.00000000e+00,  0.00000000e+00,
        -5.87753363e-02,  2.40554287e-02, -6.69894207e-01,
         9.20377561e-01,  3.63651254e+02,  0.00000000e+00,
         9.71624573e+01, -1.06413326e-01, -4.91495147e-03,
         0.00000000e+00],
       [ 5.38569168e+00,  0.00000000e+00,  0.00000000e+00,
        -7.86294313e-02, -7.15622348e-01, -1.32687469e+01,
         1.57402821e+01,  6.65223051e+02,  0.00000000e+00,
         8.16101867e+01, -2.13691629e-01, -1.32455927e-02,
         0.00000000e+00],
       [ 1.86912218e+01,  0.00000000e+00,  0.00000000e+00,
        -5.51707195e-01, -4.20034327e-02, -2.58725354e-01,
         2.21930976e+00,  4.34480644e+02,  0.00000000e+00,
         1.38221916e+01, -1.21869570e-01, -9.29740571e-03,
         0.00000000e+00],
       [ 7.35319423e+00,  0.00000000e+00,  0.00000000e+00,
        -6.62649472e-01, -8.11131984e-01, -1.87996528e+01,
         9.39951937e+00,  2.16014767e+02,  0.00000000e+00,
         2.54543602e+00, -4.58646714e+00, -3.66668975e-02,
         0.00000000e+00],
       [ 4.89339727e+00,  0.00000000e+00,  0.00000000e+00,
        -7.69420187e-01,  9.42223054e-02,  8.44599576e+00,
        -3.77831764e+00,  1.98304115e+02,  0.00000000e+00,
         8.67966706e+01, -3.21721278e-01, -2.38963376e-02,
         0.00000000e+00],
       [ 5.80305612e+00,  0.00000000e+00,  0.00000000e+00,
         9.89370494e-02, -7.13206309e-01,  7.73066098e+00,
        -2.91195690e+00,  9.29696648e+02,  0.00000000e+00,
         6.08800732e+01, -1.28035280e+00, -2.10314391e-04,
         0.00000000e+00],
       [ 1.89173147e+01,  0.00000000e+00,  0.00000000e+00,
         4.90138221e-02, -4.91295528e-01,  1.00756926e+00,
        -1.10649257e+00,  2.10119081e+02,  0.00000000e+00,
         2.70312188e+00, -4.92344461e+00, -3.62836440e-01,
         0.00000000e+00],
       [ 9.25547473e+00,  0.00000000e+00,  0.00000000e+00,
         4.84441928e-02, -9.17306128e-01,  2.47103756e+01,
        -2.30763274e+01,  8.54489415e+02,  0.00000000e+00,
         9.96974396e+01, -1.75174877e-01, -4.23146223e-04,
         0.00000000e+00],
       [ 1.40603812e+01,  0.00000000e+00,  0.00000000e+00,
        -4.73905477e-02, -1.65150229e-01, -5.73998648e+00,
         6.34880149e+00,  4.24250463e+02,  0.00000000e+00,
         9.89173340e+01, -8.71428954e-03, -2.23170391e-01,
         0.00000000e+00],
       [ 6.94994940e+00,  0.00000000e+00,  0.00000000e+00,
         7.24661260e-02, -8.74778180e-01,  7.47225206e+00,
        -2.19000884e+00,  3.12357270e+01,  0.00000000e+00,
         4.62071841e+01, -8.42173313e-01, -4.72494267e-04,
         0.00000000e+00],
       [ 7.04144956e+00,  0.00000000e+00,  0.00000000e+00,
         4.37731676e-02, -9.55095702e-01,  6.03018392e+00,
         1.46208344e+00,  1.30652259e+00,  0.00000000e+00,
         9.98684489e+01, -1.99830649e+00, -5.26931681e-04,
         0.00000000e+00],
       [ 1.31713465e+01,  0.00000000e+00,  0.00000000e+00,
        -5.25480461e-01, -2.94999709e-01,  2.16440874e+01,
        -2.44671921e+01,  6.46601160e+00,  0.00000000e+00,
         8.93470017e+01, -8.19144900e-02, -9.64452119e-04,
         0.00000000e+00],
       [ 8.13102819e+00,  0.00000000e+00,  0.00000000e+00,
         8.61833684e-02, -8.63911299e-01,  1.08817269e+00,
         2.81457922e+00,  3.14835531e+02,  0.00000000e+00,
         4.17500917e+01, -4.22868725e+00, -5.22433711e-02,
         0.00000000e+00],
       [ 2.03735711e+00,  0.00000000e+00,  0.00000000e+00,
        -1.53747258e-01, -9.49330415e-01,  1.09543679e+01,
        -6.22677733e+00,  9.72455886e+02,  0.00000000e+00,
         3.31052805e+01, -9.01679089e-02, -2.51641995e-03,
         0.00000000e+00],
       [ 1.94084646e+01,  0.00000000e+00,  0.00000000e+00,
        -3.50658349e-01,  1.34533128e-01, -5.36314336e+00,
         5.94517393e+00,  5.14690137e+02,  0.00000000e+00,
         9.58265169e+01, -7.39585596e-01, -1.44242363e-02,
         0.00000000e+00]])

# PC parameters
affparamsFA2 = np.array([[ 5.33821506e+00,  0.00000000e+00,  0.00000000e+00,
         5.68874510e+01, -4.89361020e+02,  8.55353555e+02,
         9.38945309e+02,  1.16455216e+01,  0.00000000e+00,
         9.25819019e+02, -3.40172571e+00, -4.72276008e-01,
         0.00000000e+00],
       [ 7.66806573e+00,  0.00000000e+00,  0.00000000e+00,
         1.05462131e+01, -5.20892151e+01,  2.54893644e+01,
         5.42935795e+02,  7.91996807e+00,  0.00000000e+00,
         7.82722470e+02, -3.81663579e+00, -9.98511200e-01,
         0.00000000e+00],
       [ 9.49592966e+00,  0.00000000e+00,  0.00000000e+00,
        -1.94391934e-01, -1.02110420e+01, -8.69730411e+00,
         1.23975580e+02,  1.84777326e+01,  0.00000000e+00,
         1.00695600e+02, -2.38568018e+00, -6.47524881e-04,
         0.00000000e+00],
       [ 3.68281095e+00,  0.00000000e+00,  0.00000000e+00,
         3.42175643e+00, -2.97878464e+02,  9.30027092e+02,
         9.99191553e+02,  7.05561772e+00,  0.00000000e+00,
         9.96258368e+02, -4.64023011e+00, -8.19737405e-01,
         0.00000000e+00],
       [ 7.08508969e+00,  0.00000000e+00,  0.00000000e+00,
        -1.37614961e+02,  6.96528722e+01,  6.43814065e+02,
        -2.30395233e+02,  3.60005633e+01,  0.00000000e+00,
         9.83275295e+02, -4.89127853e+00, -2.82364953e-02,
         0.00000000e+00]])


affidSA1 = ['140827DPZ U02SAI',
 '131003GG U01 SAI',
 '130809LRF U01 SAI',
 '130925RLM U01 SAI',
 '140530SMB U01SAI']

affidSA2 = ['140522AHH U02SAII',
 '131205AYK U01SAII',
 '130828CKL U01SAII',
 '140819GG U01SAII',
 '120710JPH U01 SAII',
 '131031LRF U02 SAII']

affidFA1 = ['130801AHH U01 FAI',
 '140522AHH U01FAI',
 '140611AJT U01FAI',
 '140312AN U01FAI',
 '130716CKL U02 FAI',
 '131219CKL U02FAI',
 '140123CKL U01FAI',
 '140122DPZ U02FAI',
 '140717DPZ U01FAI',
 '131031LRF U01 FAI',
 '140403LRF U02FAI',
 '140514LRF U01FAI',
 '120405MEG U01FAI',
 '140725PS U01FAI',
 '140530SMB U02FAI']

affidFA2 = ['140813AHH U02FAII',
 '140424CKL U01FAII',
 '140827DPZ U01FAII',
 '140514LRF U02FAII',
 '130925RLM U02 FAII']

affregSA1 = ['AMi', 'ALa', 'T2_t', 'T2_t', 'AMi']
affregSA2 = ['MMi', 'T1', 'MLa', 'MMi', 'MLa', 'HL']
affregFA1 = ['ALa',
 'T2_t',
 'ALa',
 'AMe',
 'T2_t',
 'MMi',
 'AMe',
 'ALa',
 'ALa',
 'ALa',
 'MMe',
 'T2_t',
 'T2_t',
 'HL',
 'ALa']
affregFA2 = ['T2_t', 'MLa', 'ALa', 'HL', 'AMi']




# parameters dictionary

affparams = {'SA1':affparamsSA1,'FA1':affparamsFA1,'FA2':affparamsFA2,'SA2':affparamsSA2}

affid = {'SA1':affidSA1,'FA1':affidFA1,'FA2':affidFA2,'SA2':affidSA2}
affreg = {'SA1':affregSA1,'FA1':affregFA1,'FA2':affregFA2,'SA2':affregSA2}

affcol = {'SA1':[0.1961,0.6275,0.1569],'FA1':[0.1176,0.4706,0.7059],
    'FA2':[1.0000,0.4980,0.],'SA2':[.5,.5,.5]}

# IH basis
ihbasis = np.array([[1., 0.96225940969727608, 0.87536423208046354, 0.766769433248516, 0.652610209235263,
   0.54205182533315932, 0.44004030458263255, 0.34898468667748422, 0.26978049353795064,
   0.20243431614165014, 0.14644660940672594, 0.10104679560404167, 0.0653373288579448,
   0.03838117154504983, 0.01925387231108916, 0.0070734240554022332, 0.0010161793388219209,
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
   0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0.0036081840668033549, 0.023350888868863606, 0.056154329924949509,
   0.098185784485027516, 0.14644660940672627, 0.19860932213786581, 0.25287986258571782,
   0.30788530192648111, 0.36258398669690095, 0.41619432759332592, 0.46813863282322443,
   0.51799889503050256, 0.565482000452344, 0.61039233748452415, 0.65261020923526325,
   0.69207480023288481, 0.72877072114331309, 0.76271736967445358, 0.79396051269637757,
   0.82256562417333257, 0.84861261407121924, 0.87219166153119332, 0.89339992639936816,
   0.91233896062573927, 0.92911267813278831, 0.94382577084072872, 0.95658248141503255,
   0.96748566135100555, 0.97663605729109038, 0.98413177980253519, 0.99006791786007275,
   0.99453626947244134, 0.99762516464606987, 0.99941936149324684, 1, 0.99944460095490972,
   0.99782709994937413, 0.99521790830721013, 0.99168399437795762, 0.98728897990622322,
   0.98209324722659574, 0.97615405387622967, 0.96952565190213669, 0.96225940969727608,
   0.9544039346526495, 0.94600519528112126, 0.93710664176824454, 0.92774932414867262,
   0.91797200750406338, 0.90781128373814834, 0.89730167961363572, 0.88647576083950341,
   0.87536423208046354, 0.86399603282680737, 0.852398429115431, 0.84059710113416641,
   0.82861622677363722, 0.8164785612154426, 0.8042055126639216, 0.79181721434220576,
   0.779332592882729, 0.76676943324851587, 0.75414444032514716, 0.74147329732476752,
   0.72877072114331309, 0.71605051481065529, 0.7033256171708524, 0.69060814992643649,
   0.67790946217681713, 0.66524017257662615, 0.65261020923526281, 0.6400288474741942,
   0.62750474555368818, 0.61504597847584586, 0.60266006996589994, 0.590354022729017,
   0.57813434707509459, 0.56600708799954591, 0.55397785080356887, 0.54205182533315954,
   0.53023380891200889, 0.51852822803943777, 0.50693915892078423, 0.49547034689400288,
   0.4841252248128099, 0.47290693044342597, 0.46181832292882552, 0.45086199837146523,
   0.44004030458263288, 0.42935535504389627, 0.41880904212362596, 0.40840304958913953,
   0.39813886445279856, 0.38801778818823174, 0.37804094735083082, 0.36820930363478938,
   0.35852366339713188, 0.34898468667748411, 0.33959289574075552, 0.33034868316834975,
   0.32125231952215072, 0.31230396060412069, 0.30350365433314042, 0.29485134725948026,
   0.28634689073617536, 0.27799004676553096, 0.26978049353795042, 0.26171783067936139,
   0.25380158422259536, 0.24603121131726063, 0.23840610469183204, 0.23092559688095471,
   0.223588964230225, 0.21639543069007172, 0.20934417140972533, 0.20243431614165014,
   0.19566495246628435, 0.18903512884639062, 0.182543857519812, 0.17619011723897821,
   0.1699728558650429, 0.16389099282413, 0.15794342143275764, 0.1521290110991424,
   0.14644660940672594, 0.1408950440859465, 0.135473124879939, 0.13017964530957116,
   0.12501338434293335, 0.11997310797412247, 0.11505757071593281, 0.11026551701080228,
   0.10559568256415164, 0.10104679560404151, 0.096617578070867238, 0.092306746740612511,
   0.088113014285022, 0.084035090271860624, 0.080071682108281583, 0.0762214959301622,
   0.072483237440124137, 0.068855612696822, 0.06533732885794491, 0.061927094879259514,
   0.0586236221719067, 0.055425625220042352, 0.052331822160825547, 0.0493409353286392,
   0.046451691765351633, 0.043662823698318642, 0.040973068987759487, 0.038381171545049886,
   0.03588588172339402, 0.033485956682281104, 0.031180160727044104, 0.028967265624786076,
   0.026846050897877005, 0.024815304096153568, 0.022873821048912835, 0.021020406097731759,
   0.019253872311088993, 0.017573041681726076, 0.015976745307634543, 0.014463823557516131,
   0.013033126221513258, 0.011683512647982897, 0.010413851867032864, 0.00922302270152009,
   0.0081099138661635539, 0.0070734240554022332, 0.0061124620205927349, 0.0052259466371155083,
   0.0044128069619275845, 0.0036719822820797665, 0.003002422154682105, 0.0024030864387886153,
   0.001872945319640773, 0.0014109793256930625, 0.0010161793388219209, 0.00068754659809966423,
   0.00042409269749704714, 0.0002248395778610135, 8.8819513496485314E-5, 1.5075093665439798E-5]])

# Sets up standard density
foot_density = {('SA1', 'T1'): 1.07, ('SA1', 'T2_t'): 6.92,('SA1', 'T3_t'): 6.92,('SA1', 'T4_t'): 6.92,('SA1', 'T5_t'): 6.92,
                ('SA1', 'MMe'): 0.27, ('SA1', 'MMi'): 0.28, ('SA1', 'MLa'): 1.64,
('SA1', 'AMe'): 0.73, ('SA1', 'AMi'): 0.69, ('SA1', 'ALa'): 2.82, ('SA1', 'HL'): 1.08,('SA1', 'HR'): 1.08,
('FA1', 'T1'): 4.62, ('FA1', 'T2_t'): 12.18, ('FA1', 'T3_t'): 12.18, ('FA1', 'T4_t'): 12.18, ('FA1', 'T5_t'): 12.18,
('FA1', 'MMe'): 1.9, ('FA1', 'MMi'): 3.38, ('FA1', 'MLa'): 5.58,
('FA1', 'AMe'): 3.63, ('FA1', 'AMi'): 2.76, ('FA1', 'ALa'): 8.67, ('FA1', 'HL'): 2.89, ('FA1', 'HR'): 2.89,
('FA2', 'T1'): 1.42, ('FA2', 'T2_t'): 1.38, ('FA2', 'T3_t'): 1.38, ('FA2', 'T4_t'): 1.38, ('FA2', 'T5_t'): 1.38,
('FA2', 'MMe'): 0.81, ('FA2', 'MMi'): 1.41, ('FA2', 'MLa'): 0.66,
('FA2', 'AMe'): 0.48, ('FA2', 'AMi'): 1.15, ('FA2', 'ALa'): 1.52, ('FA2', 'HL'): 1.20, ('FA2', 'HR'): 1.20,
('SA2', 'T1'): 1.42, ('SA2', 'T2_t'): 2.77, ('SA2', 'T3_t'): 2.77, ('SA2', 'T4_t'): 2.77, ('SA2', 'T5_t'): 2.77,
('SA2', 'MMe'): 1.90, ('SA2', 'MMi'): 1.41, ('SA2', 'MLa'): 3.28,
('SA2', 'AMe'): 1.94, ('SA2', 'AMi'): 1.61, ('SA2', 'ALa'): 2.38, ('SA2', 'HL'): 1.45, ('SA2', 'HR'): 1.45}

# Parameters for changing origin of plot foot
foot_orig = np.array([123.47860963, 426.88502674])
foot_pxl_per_mm = 2.33
foot_theta = 0.1

# Adds location tags for each area
foot_tags=['T1','T2_t','T3_t','T4_t','MMi','MMe','T5_t','MLa','AMe','AMi','ALa','HL','HR']
