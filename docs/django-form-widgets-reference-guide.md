# Django Form Widgets Reference Guide

Django forms provide a powerful and flexible way to control the presentation and functionality of form fields. One key feature is the ability to customize how form fields are rendered using widgets. This guide provides an overview of how to define and customize widgets in Django forms.

## Basic Widget Usage

A widget in Django is a Python class that renders itself as an HTML input element. The widget controls the appearance and behavior of a field in the browser.

### Defining a Widget in a Form Field

You can explicitly define a widget for a form field by setting the `widget` attribute in the field's constructor:

```python
from django import forms

class MyForm(forms.Form):
    my_field = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-class'}))
```

## Customizing Widgets in ModelForms

For forms tied to models (`ModelForm`), you can customize widgets for the fields generated from the model. This is done using the `widgets` attribute of the form's inner `Meta` class.

### Using the `widgets` Meta Option

You can specify custom widgets for model fields without redefining the entire field:

```python
from django.forms import ModelForm, Textarea
from .models import MyModel

class MyModelForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2']
        widgets = {
            'field1': Textarea(attrs={'cols': 40, 'rows': 10}),
        }
```

## Common Widgets and Their Customizations

Here are some common widgets and ways to customize them:

### `TextInput`

A basic text input field.

```python
forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter text'})
```

### `Textarea`

A multi-line text input field.

```python
forms.Textarea(attrs={'cols': 40, 'rows': 5})
```

### `Select`

A dropdown menu.

```python
forms.Select(choices=MY_CHOICES, attrs={'class': 'select-field'})
```

### `CheckboxInput`

A single checkbox.

```python
forms.CheckboxInput(attrs={'class': 'checkbox'})
```

### `RadioSelect`

A group of radio buttons.

```python
forms.RadioSelect(choices=MY_CHOICES)
```

### `SelectMultiple`

A multi-select field (allows multiple selections).

```python
forms.SelectMultiple(attrs={'class': 'multi-select'})
```

## Advanced Customizations

For more complex customizations, you can subclass existing widgets or create your own widget classes.

### Creating a Custom Widget

To create a custom widget, you typically subclass `forms.Widget` or one of its subclasses:

```python
from django import forms

class CustomWidget(forms.TextInput):
    template_name = 'path/to/custom_template.html'
```

In the custom widget, you can define a specific template or add custom rendering logic.

---

This reference guide provides a starting point for working with widgets in Django forms. For more advanced use cases, consult the [Django documentation on form widgets](https://docs.djangoproject.com/en/stable/ref/forms/widgets/).