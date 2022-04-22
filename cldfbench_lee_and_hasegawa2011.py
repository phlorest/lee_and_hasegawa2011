import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "lee_and_hasegawa2011"

    def cmd_makecldf(self, args):
        self.init(args)

        summary = self.raw_dir.read_tree(
            'phylogeny_japonic.tre', detranslate=True)
        args.writer.add_summary(summary, self.metadata, args.log)
        
        posterior = self.raw_dir.read_trees(
            'Japonic_COV_UCLD.trees.gz',
            burnin=2000, sample=1000, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('Japonic.nex'),
            self.characters, 
            args.log)
