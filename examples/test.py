import time  # Generated by Copilot

import pandas as pd

from navidiv import (
    FGscorer,
    Ngram_scorer,
    Scaffold_scorer,
    cluster_similarity_scorer,
    orginal_similarity_scorer,
    ring_scorer,
)
from navidiv.fragment import (
    fragment_scorer,
    fragment_scorer_matching,
)
from navidiv.utils import get_smiles_column


def test_fragment_match_scorer(smiles_list, scores):
    """Test the fragment match scorer."""
    frag_match_score = fragment_scorer_matching.FragmentMatchScorer(
        output_path="/media/mohammed/Work/Navi_diversity/examples/resultstest/",
        min_count_fragments=1,
    )
    start = time.time()  # Generated by Copilot
    scores_frag_match = frag_match_score.get_score(
        smiles_list=smiles_list,
        scores=scores,
    )
    end = time.time()  # Generated by Copilot
    print(
        f"FragmentMatchScorer.get_score time: {end - start:.3f} seconds"
    )  # Generated by Copilot
    print("Fragment Match scores")
    print("scores", scores_frag_match)
    return scores_frag_match


def test_orginal_scorer(smiles_list, scores):
    """Test the original similarity scorer."""
    df_original = pd.read_csv(
        "/media/mohammed/Work/Navi_diversity/examples/df_original.csv"
    )
    smiles_list_to_compare_to = df_original["smiles"].tolist()
    # print(smiles_list_to_compare_to)
    orginal_score = orginal_similarity_scorer.OriginalSimScorer(
        output_path="/media/mohammed/Work/Navi_diversity/examples/resultstest/",
        threshold=0.3,
        smiles_list_to_compare_to=smiles_list_to_compare_to,
    )
    start = time.time()  # Generated by Copilot
    scores_orginal = orginal_score.get_score(
        smiles_list=smiles_list,
        scores=scores,
    )
    end = time.time()  # Generated by Copilot
    print(
        f"OriginalSimilarityScorer.get_score time: {end - start:.3f} seconds"
    )  # Generated by Copilot
    print("Original scores")
    print("scores", scores_orginal)
    return scores_orginal


def test_scaffold_scorer(smiles_list, scores):
    """Test the scaffold scorer."""
    scaffold_score = Scaffold_scorer.Scaffold_scorer(
        output_path="/media/mohammed/Work/Navi_diversity/examples/resultstest/",
        scaffold_type="csk_bm",
    )
    start = time.time()  # Generated by Copilot
    scores_scaffold = scaffold_score.get_score(
        smiles_list=smiles_list,
        scores=scores,
    )
    end = time.time()  # Generated by Copilot
    print(
        f"ScaffoldScorer.get_score time: {end - start:.3f} seconds"
    )  # Generated by Copilot
    print("Scaffold scores")
    print("scores", scores_scaffold)
    return scores_scaffold


def test_cluster_scorer(smiles_list, scores):
    """Test the cluster similarity scorer."""
    cluster_score = cluster_similarity_scorer.ClusterSimScorer(
        output_path="/media/mohammed/Work/Navi_diversity/examples/resultstest/",
        threshold=0.25,
    )
    start = time.time()  # Generated by Copilot
    scores_cluster = cluster_score.get_score(
        smiles_list=smiles_list,
        scores=scores,
    )
    end = time.time()  # Generated by Copilot
    print(
        f"ClusterSimilarityScorer.get_score time: {end - start:.3f} seconds"
    )  # Generated by Copilot
    print("Cluster scores")
    print("scores", scores_cluster)
    return scores_cluster


def test_ring_scorer(smiles_list, scores):
    """Test the ring scorer."""
    ring_score = ring_scorer.RingScorer(
        output_path="/media/mohammed/Work/Navi_diversity/examples/resultstest/",
    )
    start = time.time()  # Generated by Copilot
    scores_ring = ring_score.get_score(
        smiles_list=smiles_list,
        scores=scores,
    )
    end = time.time()  # Generated by Copilot
    print(
        f"RingScorer.get_score time: {end - start:.3f} seconds"
    )  # Generated by Copilot
    print("Ring scores")
    print("scores", scores_ring)
    return scores_ring


def test_fragment_scorer(smiles_list, scores):
    """Test the fragment scorer."""
    frag_score = fragment_scorer.FragmentScorer(
        min_count_fragments=1,
        output_path="/media/mohammed/Work/Navi_diversity/examples/resultstest/",
    )
    start = time.time()  # Generated by Copilot
    scores = frag_score.get_score(
        smiles_list=smiles_list,
        scores=scores,
    )
    end = time.time()  # Generated by Copilot
    print(
        f"FragmentScorer.get_score time: {end - start:.3f} seconds"
    )  # Generated by Copilot
    print("Fragment scores")
    print("scores", scores)
    return scores


def test_ngram_scorer(smiles_list, scores):
    """Test the ngram scorer."""
    ngram_score = Ngram_scorer.NgramScorer(
        ngram_size=10,
        output_path="/media/mohammed/Work/Navi_diversity/examples/resultstest/",
    )
    start = time.time()  # Generated by Copilot
    scores_ngram = ngram_score.get_score(
        smiles_list=smiles_list,
        scores=scores,
    )
    end = time.time()  # Generated by Copilot
    print(
        f"NgramScorer.get_score time: {end - start:.3f} seconds"
    )  # Generated by Copilot
    print("Ngram scores")
    print("scores", scores_ngram)
    return scores_ngram


def test_fg_scorer(smiles_list, scores):
    """Test the FG scorer."""
    fg_score = FGscorer.FGScorer(
        output_path="/media/mohammed/Work/Navi_diversity/examples/resultstest/",
    )
    start = time.time()  # Generated by Copilot
    scores_fg = fg_score.get_score(
        smiles_list=smiles_list,
        scores=scores,
    )
    end = time.time()  # Generated by Copilot
    print(
        f"FGScorer.get_score time: {end - start:.3f} seconds"
    )  # Generated by Copilot
    print("FG scores")
    print("scores", scores_fg)
    return scores_fg


if __name__ == "__main__":
    csv_file = "/media/mohammed/Work/Navi_diversity/reinvent_runs/runs/test/test2/stage0/results/clusters/groupby_results_clusters.csv"
    df = pd.read_csv(csv_file).sample(frac=0.1).reset_index(drop=True)
    # df = df[df["step"] == 1000]
    print("columns", df.columns)
    smiles_col = get_smiles_column(df)
    df = df.dropna(subset=[smiles_col])
    smiles_list = df[smiles_col].tolist()
    scores = df["median_score_fragment_mean"].tolist()
    print("will process", len(smiles_list), "smiles")
    print("will process", len(scores), "scores")
    test_fragment_match_scorer(smiles_list, scores)
    # test_fg_scorer(smiles_list, scores)
    # test_ngram_scorer(smiles_list, scores)
    # test_ring_scorer(smiles_list, scores)
    # test_cluster_scorer(smiles_list, scores)
    # test_scaffold_scorer(smiles_list, scores)
    # test_fragment_scorer(smiles_list, scores)
    print("done")
