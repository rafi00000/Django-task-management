from django import forms
from tasks.models import Task, TaskDetail

# django form normal.
# class TaskForm(forms.Form):
#     title = forms.CharField(max_length=250)
#     description = forms.CharField(widget=forms.Textarea)
#     due_date = forms.DateField(widget=forms.SelectDateWidget)
#     assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[])

#     def __init__(self, *args, **kwargs):
#         employees = kwargs.pop("employees", [])
#         super().__init__(*args, **kwargs)
#         self.fields['assigned_to'].choices = [(emp.id, emp.name) for emp in employees]
        

# Style Mixin
class StyleFormMixin:
    """Mixin class to add style to form fields"""
    default_classes = "border border-2 border-black p-2 mb-2"

    def apply_styled_widget(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                print("powchaisi")
                field.widget.attrs.update({
                    'class': f"{self.default_classes}",
                    'placeholder': f'Enter {field_name}'
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f'Enter {field_name}',
                    'rows': 5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': self.default_classes
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': self.default_classes
                })
# django Model Form

class TaskModelForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']

        """using mixin widget class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widget()


class TaskDetailModelForm(StyleFormMixin ,forms.ModelForm):
    class Meta:
        model = TaskDetail
        fields = ['priority']

        """using mixin widget class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widget()