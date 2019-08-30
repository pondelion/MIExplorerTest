from typing import List, Dict
from ..base_api_helper import BaseApiHelper


class VaspCalculated(BaseApiHelper):
    """Materials Project's Material API helper class
        for calculated materials data by vasp.

    Example:
        >>> from materials_project.api_helper import VaspCalculated
        >>> vc = VaspCalculated()
        >>> res = vc.fetch({'material_specifier': 'Cu', 'property': 'structure'})
    """

    def __init__(self):
        super().__init__()
        self._REQUIRED_KEYS = ['material_specifier', 'property']
        self._AVAILABLE_PROPERTY_LIST = {
            'pretty_formula': 'A nice formula where the element amounts are normalized',
            'unit_cell_formula': 'The full explicit formula for the unit cell',
            'icsd_ids': "List of Inorganic Crystal Structure Database (ICSD) ids for structures"
                        "that have been deemed to be structurally similar to this material"
                        "based on pymatgen's StructureMatcher algorithm, if any.",
            'energy': 'Calculated vasp energy for structure',
            'energy_per_atom': 'Calculated vasp energy normalized to per atom in the unit cell',
            'volume': 'Final relaxed volume of the material',
            'density': 'Final relaxed density of the material',
            'nsites': 'Number of sites in the unit cell',
            'elements': 'A array of the elements in the material',
            'nelements': 'The number of elements in the material',
            'spacegroup': 'An associative array containing basic space group information.',
            'initial_structure': 'The initial input structure for the calculation in the pymatgen'
                                 ' json representation (see later section).',
            'final_structure': 'The final relaxed structure in the pymatgen json representation (see later section).',
            'structure': 'An alias for final_structure.',
            'cif': 'A string containing the structure in the CIF format.',
            'formation_energy_per_atom': 'Calculated formation energy from the elements normalized'
                                         ' to per atom in the unit cell',
            'e_above_hull': 'Calculated energy above convex hull for structure. Please see'
                            ' Phase Diagram Manual for the interpretation of this quantity.',
            'elasticity': 'Mechanical properties in the elastic limit. Contains the full elastic
                          ' tensor as well as derived properties, e.g. Poisson ratio and bulk (K)'
                          ' and shear (G) moduli. Consult our hierarchical documentation for the'
                          ' particular names of sub-keys.',
            'is_hubbard': 'A boolean indicating whether the structure was calculated using'
                          ' the Hubbard U extension to DFT',
            'hubbards': 'An array of Hubbard U values, where applicable.',
            'is_compatible': 'Whether this calculation is considered compatible under the GGA/GGA+U mixing scheme.',
            'band_gap': 'The calculated band gap',
            'dos': 'The calculated density of states in the pymatgen json representation',
            'bandstructure': 'The calculated "line mode" band structure (along selected symmetry'
                             ' lines -- aka "branches", e.g. \Gamma to Z -- in the Brillouin zone)'
                             ' in the pymatgen json representation',
            'bandstructure_uniform': 'The calculated uniform band structure in the pymatgen json representation',
            'entry': 'This is a special property that returns a pymatgen ComputedEntry in the json representation.'
                     ' ComputedEntries are the basic unit for many structural and thermodynamic analyses in the pymatgen code base.',
            'total_magnetization': 'total magnetic moment of the unit cell',
        }

    def _get_api_url_fmt(self) -> str:
        return 'https://www.materialsproject.org/rest/v2/materials/{material_specifier}/vasp/{property}'

    def get_required_keywards(self) -> List[str]:
        return self._REQUIRED_KEYS

    def get_available_property_list(
        self,
        description: bool=False
    ) -> List[str] | Dict[str, str]:
        if description:
            return self._AVAILABLE_PROPERTY_LIST
        else:
            return list(self._AVAILABLE_PROPERTY_LIST.keys())
