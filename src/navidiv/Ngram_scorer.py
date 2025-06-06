# Generated by Copilot

import pandas as pd

from navidiv.scorer import BaseScore


class NgramScorer(BaseScore):
    """Handles fragment scoring and analysis for molecular datasets."""

    def __init__(
        self,
        ngram_size: int = 10,
        output_path: str | None = None,
    ) -> None:
        """Initialize FragmentScore.

        Args:
            min_count_fragments (int): Minimum count for fragments to be
                considered.
            output_path (str | None): Path to save output files.
        """
        super().__init__(output_path=output_path)
        self._min_count_fragments = 10
        self._csv_name = f"ngrams_{ngram_size}"
        self.ngram_size = ngram_size
        self.add_num_atoms  = False

    def get_count(self, smiles_list: list[str]) -> tuple[pd.DataFrame, None]:
        """Calculate the percentage of each fragment in the dataset.

        Args:
            smiles_list (list[str]): List of SMILES strings.

        Returns:
            tuple: DataFrame with fragment info, None (for compatibility)
        """
        ngrams = []
        for smiles in smiles_list:
            ngrams.extend(
                [
                    smiles[i : i + self.ngram_size]
                    for i in range(len(smiles) - self.ngram_size + 1)
                ]
            )

        fragments, over_represented_fragments = self._from_list_to_count_df(
            smiles_list,
            ngrams,
        )
        self._fragments_df = fragments
        return fragments, over_represented_fragments

    def _count_substructure_in_smiles(self, smiles_list, ngram):
        """Check if ngram is in smiles"""
        return len([smiles for smiles in smiles_list if ngram in smiles])

    def _comparison_function(
        self,
        smiles: str | None = None,
        fragment: str | None = None,
        mol=None,
    ) -> bool:
        """Check if the fragment is present in the SMILES string or molecule."""
        if smiles is None:
            return False

        if fragment is None:
            return False

        return fragment in smiles
