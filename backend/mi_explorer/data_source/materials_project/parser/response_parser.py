

class VaspResponseParser:

    @classmethod
    def parse_structure(cls, res):
        structures = []

        for r in res:
            mat = r['structure']['lattice']['matrix']
            sites = {}
            for site in r['structure']['sites']:
                if site['species'][0]['element'] not in sites:
                    sites[site['species'][0]['element']] = []
                sites[site['species'][0]['element']].append(site['xyz'])
            structures.append({
                'material_id': cls._validate(r, 'material_id'),
                'matrix': mat,
                'sites': sites
            })

        return structures

    @classmethod
    def parse_basic_propaties(cls, res):

        basic_properties = [{
            'material_id': cls._validate(r, 'material_id'),
            'energy': cls._validate(r, 'energy'),
            'energy_per_atom': cls._validate(r, 'energy_per_atom'),
            'volume': cls._validate(r, 'volume'),
            'density': cls._validate(r, 'density'),
            'nsites': cls._validate(r, 'nsites'),
            'nelements': cls._validate(r, 'nelements'),
        } for r in res]

        return basic_properties

    @classmethod
    def parse_thermodynamic_propaties(cls, res):

        thermodynamic_properties = [{
            'material_id': cls._validate(r, 'material_id'),
            'formation_energy_per_atom': cls._validate(r, 'formation_energy_per_atom'),
            'e_above_hull': cls._validate(r, 'e_above_hull'),
        } for r in res]

        return thermodynamic_properties

    @classmethod
    def parse_mechanical_propaties(cls, res):

        mechanical_properties = [{
            'material_id': cls._validate(r, 'material_id'),
            'elasticity': cls._validate(r, 'elasticity'),
            'piezo': cls._validate(r, 'piezo'),
            'diel': cls._validate(r, 'diel'),
        } for r in res]

        return mechanical_properties

    @classmethod
    def parse_electrical_propaties(cls, res):

        electrical_properties = [{
            'material_id': cls._validate(r, 'material_id'),
            'band_gap_energy': cls._validate(cls._validate(r, 'band_gap'), 'energy'),
        } for r in res]

        return electrical_properties

    @classmethod
    def parse_magnetic_propaties(cls, res):

        magnetic_properties = [{
            'material_id': cls._validate(r, 'material_id'),
            'total_magnetization': cls._validate(r, 'total_magnetization'),
        } for r in res]

        return magnetic_properties

    @classmethod
    def _validate(cls, res, key: str):
        return res[key] if key in res else None
