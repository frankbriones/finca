from django import forms
from betterforms.multiform import MultiModelForm

from usr.models import Roles, Usuarios, UsuariosGrupos, TipoUsuario
from django.contrib.auth.models import *



class GrupoForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = []

class RolForm(forms.ModelForm):

    class Meta:
        model = Roles
        fields = '__all__'
        exclude = []
        labels = {'descripcion': 'Descripcion del Rol'}
        widget = {'descripcion': forms.TextInput}


class RolGrupoForm(MultiModelForm):
    form_classes = {
        'grupo': GrupoForm,
        'rol': RolForm,
    }



#formulario para la edicion de perfil de usuario logeado
class EditarUsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'telefono',
            'img_perfil',
            'usuario_telegram'
        ]
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class EditarPerfilForm(forms.ModelForm):

    def __init__( self, *args, **kwargs ):
        super(EditarPerfilForm, self ).__init__( *args, **kwargs )
        self.fields['tipo_usuario'] = forms.ModelChoiceField(queryset = TipoUsuario.objects.exclude(descripcion='ADMINISTRADOR'))
        excluir_roles = ['ADMINISTRADOR', 'PROVEEDOR']
        self.fields['rol'] = forms.ModelChoiceField(queryset = Roles.objects.exclude(descripcion__in=excluir_roles))
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        

    class Meta:
        model = Usuarios
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'telefono',
            'img_perfil',
            'usuario_telegram',
            'rol',
            'tipo_usuario'
        ]
 


class AsignarGrupoForm(forms.ModelForm):

    class Meta:
        model = UsuariosGrupos
        fields = []

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            print(field)
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })



class UsuarioGrupoForm(MultiModelForm):
    form_classes = {
        'usuario': EditarPerfilForm,
        'grupo': AsignarGrupoForm
    }




# class SignupForm(forms.Form):
#    """Sign up form."""
#    nombres = forms.CharField(min_length=2, max_length=50, label= 'Nombres')
#    apellidos = forms.CharField(min_length=2, max_length=50, label= 'Apellidos')
#    email = forms.CharField(
#        min_length=6,
#        max_length=70,
#        widget=forms.EmailInput()
#   )
#    password = forms.CharField(
#        max_length=70,
#        widget=forms.PasswordInput(),
#        help_text=password_validation.password_validators_help_text_html(),
#    )
#    password_confirmation = forms.CharField(
#        max_length=70,
#        widget=forms.PasswordInput(),
#        label='Confirmacion de Password'
#    )

#    celular = forms.CharField(
#        widget=forms.TextInput(),
#        max_length=10,
#        label='Movil'
#    )
      


#    def clean_email(self):
#        """Username must be unique."""
#        email = self.cleaned_data['email']
#        username = email
#        email_taken = Profile.objects.filter(email=email).exists()
#        if email_taken:
#            raise forms.ValidationError('Correo se encuentra en uso.')
#        return email

#    def clean(self):
#        """Verify password confirmation match."""
#        data = super().clean()

#        password = self.cleaned_data['password']
#        password_confirmation = self.cleaned_data['password_confirmation']

#        if password != password_confirmation:
#            raise forms.ValidationError(
#                _('password no coinciden')

#                )
#        if password:
#             try:
#                 password_validation.validate_password(password)
#             except forms.ValidationError as error:
#                 self.add_error('password_confirmation', error)
#        return data


#    def save(self):	
#        """Create user and profile."""
#        data = self.cleaned_data
#        data.pop('password_confirmation')

#        profile = Profile.objects.create_user(**data)
#        from talleres.models import Estudiante
#        estudiante = Estudiante.objects.create(usuario=profile)
#        self.send_confirmation_email(profile)
#        profile.save()
#    def send_confirmation_email(self, user):
#       user = Profile.objects.get(pk=user.id)
#       verification_token = self.genera_token_verificado(user)
#       subject  = 'Bienvenido, {} verifica tu cuenta.'.format(user.email)
#       from_email = 'Tacita Caliente <primer1grupo@gmail.com>'
#       content = render_to_string(
#         'emails/user/account_verification.html',
#         {'token': verification_token, 'user': user}
#         )
#       msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
#       msg.attach_alternative(content, "text/html")
#       msg.send()
#    def genera_token_verificado(self, user):
#     # return'abc'
#       print(user)
#       exp_date = datetime.now() + timedelta(days=3)
#       payload = {
#       'user': user.id,
#       'exp': int(exp_date.timestamp()),
#       'type': 'email_confirmation'
#       }
#       token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
#       return token.decode()