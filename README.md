# nectec-bert
python ./fairseq-nectec/fairseq_cli/preprocess.py --trainpref test/train.txt --testpref test/test.txt --validpref test/test.txt --destdir test/data-bin --only-source --joined-dictionary --nwordssrc 10000

512
2048
500
50000
--num-workers 8
fairseq-train --task masked_lm test/data-bin --save-dir test/roberta --arch roberta --dropout 0.1  --optimizer adam --adam-betas '(0.9, 0.98)' --weight-decay 0.01 --clip-norm 0.0 --lr 1e-4 --lr-scheduler inverse_sqrt --warmup-updates 10000 --warmup-init-lr 1e-4 --tokens-per-sample 64 --max-tokens 128 --update-freq 16 --save-interval-updates 10 --keep-interval-updates 10 --keep-last-epochs 10 --criterion masked_lm --skip-invalid-size-inputs-valid-test --bpe sentencepiece --sentencepiece-vocab=test/sentencepiece.bpe.model --sample-break-mode complete_doc --mask-whole-words --dataset-impl mmap --max-update 20

fairseq-train --task legacy_masked_lm test/data-bin --save-dir test/bert --arch bert_base --dropout 0.1  --optimizer adam --adam-betas '(0.9, 0.98)' --weight-decay 0.01 --clip-norm 0.0 --lr 1e-4 --lr-scheduler inverse_sqrt --warmup-updates 10000 --warmup-init-lr 1e-4 --tokens-per-sample 64 --max-tokens 128 --update-freq 16 --save-interval-updates 10 --keep-interval-updates 10 --keep-last-epochs 10 --criterion legacy_masked_lm_loss --skip-invalid-size-inputs-valid-test --bpe sentencepiece --sentencepiece-vocab=test/sentencepiece.bpe.model --dataset-impl mmap --max-update 20

python ../fairseq/scripts/average_checkpoints.py --inputs roberta --num-update-checkpoints 5 --output roberta/average-model.pt

python ../fairseq/scripts/average_checkpoints.py --inputs bert --num-update-checkpoints 5 --output bert/average-model.pt

fairseq-validate data-bin --path roberta/average-model.pt --max-sentences 2 --tokens-per-sample 64

fairseq-validate data-bin --path bert/average-model.pt --max-sentences 2 --tokens-per-sample 64
