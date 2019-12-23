#!/usr/bin/env python
# encoding: utf-8
'''
@author: zessay
@license: (C) Copyright Sogou.
@contact: zessay@sogou-inc.com
@file: __init__.py.py
@time: 2019/12/17 16:32
@description: https://github.com/jadore801120/attention-is-all-you-need-pytorch/blob/master/transformer
'''
from snlp.modules.transformer.sublayers import ScaledDotProductAttention, PositionwiseFeedForward, MultiHeadAttention
from snlp.modules.transformer.layers import EncoderLayer, DecoderLayer
from snlp.modules.transformer.models import Encoder, Decoder, Transformer, StackedEncoder
from snlp.modules.transformer.translator import Translator
