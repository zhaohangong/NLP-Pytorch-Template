python run_multiqa.py \
  --model_name=msn \
  --fixed_length_uttr=20 \
  --fixed_length_resp=20 \
  --fixed_length_turn=5 \
  --l2_reg=1e-3 \
  --epochs=20 \
  --batch_size=128 \
  --lr=1e-4 \
  --seed=2020 \
  --optimizer=adamw \
  --cuda_num=2 \
  --is_load_preprocessor