from openfermion_dirac import MolecularData_Dirac, run_dirac
from openfermion.transforms import jordan_wigner
from openfermion.utils import eigenspectrum
import os

# Set molecule parameters.
basis = 'STO-3G'
bond_length = 1.0
multiplicity = 1
charge = 0
data_directory=os.getcwd()

delete_input = True
delete_xyz = True
delete_output = False
delete_MRCONEE = True
delete_MDCINT = True
delete_FCIDUMP = False
# a ghost nuclei "foo" is added to lower the symmetry.
geometry = [('H', (0., 0., 0.)), ('H', (0., 0., bond_length))]
propint = "ZDIPLEN"

print()
print('#'*40)
print('NONREL Dirac calculation')
print('#'*40)
print()
run_ccsd = True
point_nucleus = True
if run_ccsd:
 description = 'R' + str(bond_length) + '_ccsd'
else:
 description = 'R' + str(bond_length) + '_scf'

molecule = MolecularData_Dirac(geometry=geometry,
                               basis=basis,
                               multiplicity=multiplicity,
                               charge=charge,
                               description=description,
                               data_directory=data_directory)

molecule = run_dirac(molecule,
                    propint=propint,
                    point_nucleus=point_nucleus,
                    delete_input=delete_input,
                    delete_xyz=delete_xyz,
                    delete_output=delete_output,
                    delete_MRCONEE=delete_MRCONEE,
                    delete_MDCINT=delete_MDCINT,
                    delete_FCIDUMP=delete_FCIDUMP,
                    run_ccsd=run_ccsd)

print("spinorbs = ",molecule.get_integrals_FCIDUMP()[1])
print('Hartree-Fock energy of {} Hartree.'.format(molecule.get_energies()[0]))
print('MP2 energy of {} Hartree.'.format(molecule.get_energies()[1]))
print('CCSD energy of {} Hartree.'.format(molecule.get_energies()[2]))
print('property integrals in the AO basis: {}'.format(molecule.get_propint()))

property_hamiltonian = molecule.get_property_hamiltonian()
qubit_hamiltonian = jordan_wigner(property_hamiltonian)
evs = eigenspectrum(qubit_hamiltonian)
print(property_hamiltonian)
print(qubit_hamiltonian)
print(evs)