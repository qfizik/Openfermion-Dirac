# Test set up for generating Hamiltonian for H2.

from openfermion_dirac import MolecularData_Dirac, run_dirac
from openfermion.hamiltonians import MolecularData
from openfermion.transforms import jordan_wigner, project_onto_sector, bravyi_kitaev
from openfermion.utils import count_qubits,eigenspectrum
import numpy as np
import os
import subprocess

# Set molecule parameters.
basis = 'sto-3g'
R = 2.0
angle = 10
angle_rad = angle*np.pi/180.0
multiplicity = 1
charge = 0
data_directory=os.getcwd()

delete_input = True
delete_xyz = True
delete_output = False
delete_MRCONEE = True
delete_MDCINT = True
delete_FCIDUMP = False
geometry = [('H', (0., R*np.sin(angle_rad), R*np.cos(angle_rad))), ('H', (0., R*np.sin(angle_rad), -R*np.cos(angle_rad))), 
            ('H', (0., -R*np.sin(angle_rad), -R*np.cos(angle_rad))), ('H', (0., -R*np.sin(angle_rad), R*np.cos(angle_rad)))]

print()
print('#'*40)
print('NONREL Dirac calculation')
print('#'*40)
print()
run_ccsd = 1
description = 'R' + str(R) + '_T' + str(angle) +  '_ccsd_dirac'

molecule = MolecularData_Dirac(geometry=geometry,
                               basis=basis,
                               multiplicity=multiplicity,
                               charge=charge,
                               description=description,
                               data_directory=data_directory)

molecule_dirac = run_dirac(molecule,
                    delete_input=delete_input,
                    delete_xyz=delete_xyz,
                    delete_output=delete_output,
                    delete_MRCONEE=delete_MRCONEE,
                    delete_MDCINT=delete_MDCINT,
                    delete_FCIDUMP=delete_FCIDUMP,
                    run_ccsd=run_ccsd)

fermion_hamiltonian = molecule_dirac.get_molecular_hamiltonian()[0]
qubit_hamiltonian_dirac = jordan_wigner(fermion_hamiltonian)
evs_dirac = eigenspectrum(qubit_hamiltonian_dirac)
print('Hartree-Fock energy of {} Hartree.'.format(molecule_dirac.get_energies()[0]))
print('MP2 energy of {} Hartree.'.format(molecule_dirac.get_energies()[1]))
print('CCSD energy of {} Hartree.'.format(molecule_dirac.get_energies()[2]))
print('Solving the Qubit Hamiltonian (Jordan-Wigner): \n {}'.format(evs_dirac))
