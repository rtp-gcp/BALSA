# weirdness with openai version

* [existing bug](https://community.openai.com/t/attributeerror-module-openai-has-no-attribute-chatcompletion/81490/20)

```
pip install --upgrade pip
pip install openai --upgrade
pip show openai
pip uninstall openai
```


Turns out the api changed.  qt_openai.ipynb has correct version.


# Model tuning and training data

* [more to it than I thought](https://platform.openai.com/docs/guides/fine-tuning/use-a-fine-tuned-model)