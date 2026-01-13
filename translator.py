from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/nllb-200-distilled-600M"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def translate(text, src_lang, tgt_lang):
    tokenizer.src_lang = src_lang
    inputs = tokenizer(text, return_tensors="pt")

    # ✅ FIX: correct way to get target language id
    tgt_lang_id = tokenizer.convert_tokens_to_ids(tgt_lang)

    outputs = model.generate(
        **inputs,
        forced_bos_token_id=tgt_lang_id,
        max_length=256
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
