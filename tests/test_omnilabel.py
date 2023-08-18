from ecole_dataset.datasets.omnilabel import OmniLabel


def test_load_omnilabel():
    ds = OmniLabel.load()
    assert ds.num_rows == 165703


if __name__ == "__main__":
    test_load_omnilabel()
