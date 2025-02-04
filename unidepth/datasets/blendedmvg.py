from typing import Any

from unidepth.datasets.sequence_dataset import SequenceDataset


class BlendedMVG(SequenceDataset):
    min_depth = 0.01
    max_depth = 5000.0
    depth_scale = 1000.0
    test_split = "train.txt"
    train_split = "train.txt"
    sequences_file = "sequences_clean.json"
    hdf5_paths = ["BlendedMVG_.hdf5"]

    def __init__(
        self,
        image_shape: tuple[int, int],
        split_file: str,
        test_mode: bool,
        normalize: bool,
        augmentations_db: dict[str, Any],
        resize_method: str,
        mini: float = 1.0,
        num_frames: int = 1,
        benchmark: bool = False,
        decode_fields: list[str] = ["image", "depth"],
        inplace_fields: list[str] = ["K", "cam2w"],
        **kwargs,
    ) -> None:
        super().__init__(
            image_shape=image_shape,
            split_file=split_file,
            test_mode=test_mode,
            benchmark=benchmark,
            normalize=normalize,
            augmentations_db=augmentations_db,
            resize_method=resize_method,
            mini=mini,
            num_frames=num_frames,
            decode_fields=decode_fields,
            inplace_fields=inplace_fields,
            **kwargs,
        )

    def pre_pipeline(self, results):
        results = super().pre_pipeline(results)
        results["dense"] = [True] * self.num_frames * self.num_copies
        results["si"] = [False] * self.num_frames * self.num_copies
        results["quality"] = [2] * self.num_frames * self.num_copies
        return results
