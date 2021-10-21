import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "lee_and_hasegawa2011"

    def cmd_makecldf(self, args):
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree_from_nexus(
                args,
                self.raw_dir / 'phylogeny_japonic.tre',
                nex,
                'summary',
                detranslate=True,
            )
        posterior = self.sample(
            self.read_gzipped_text(self.raw_dir / 'Japonic_COV_UCLD.trees.gz'),
            detranslate=True,
            as_nexus=True)

        with self.nexus_posterior() as nex:
            for i, tree in enumerate(posterior.trees.trees, start=1):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i))

        self.add_data(args, self.raw_dir / 'Japonic.nex')
