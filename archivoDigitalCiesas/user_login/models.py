from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class areaUsuario(models.Model):
    areas = (
        ('DG','Direccion General'),
          ('DA','Dirección Academica'),
            ('SDI','Subdirección de Investigación'),
              ('CINT','Coordinación de Intercambios'),
              ('CPRO','Coordinación de Proyectos'),
            ('SDD','Subdirección de Docencia'),
              ('CSE','Coordinación de Servicios Escolares'),
              ('PCDMX','Posgrado en la CDMX'),
              ('PLNGT','Posgrado en LINGÜÍSTICA'),
              ('POCCI','Posgrado en OCCIDENTE'),
              ('PSURE','Posgrado en SURESTE'),
              ('PGOLF','Posgrado en GOLFO'),
              ('PPENI','Posgrado en PENINSULAR'),
              ('PNORE','Posgrado en NORESTE'),
            ('SDB','Subdirección de Bibliotecas'),
            ('SDDP','Subdirección de Difusión y Publicaciones'),
              ('CPUB','Coordinación de Publicaciones'),
              ('CDIF','Coordinación de difusión'),
            ('SDINF','Subdirección de Informática'),
              ('CSIS','Coordinación de Sistemas'),
          ('DV','Dirección de Vinculación'),
          ('DADMN','Dirección de Administración'),
            ('CPLYC','Coordinación de Planeación y Control'),
            ('UTRNS','Unidad de Trasparencia'),
            ('SDRH','Subdirección de Recursos Financieros'),
              ('JFPR','Jefatura de Presupuestos'),
              ('JFCO','Jefatura de Contabilidad'),
              ('JFRH','Jefatura de Recursos Humanos'),
              ('JFSG','Jefatura de Servicios Generales'),
              ('JFRM','Jefatura de Recursos Materiales'),
              ('CARC','Coordinación de Archivo'),
              ('CAFP','Coordinación de Admin Financiera de Proyectos'),
        ('UR','Unidades Regionales'),
          ('DRG','Dirección Regional Golfo'),
          ('DRPS','Dirección Regional Pacifico Sur	'),
          ('DRS','Dirección General Sureste	'),
          ('DRO','Dirección General Occidente	'),
          ('DRPN','Dirección Regional Peninsular	'),
          ('DRN','Dirección Regional Noreste	'),
            ('JFAD','Jefatura de Administración'),
            ('JFBI','Jefatura de Biblioteca'),
    )
    area = models.CharField(
        max_length=10,
        choices=areas,
        default='DG',
    )

    def __str__(self):
        return self.area

class usuarioFinal(models.Model):

    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    area = models.ForeignKey('areaUsuario',on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    cargo = models.CharField(max_length=254)
    telefono = models.IntegerField()
    ext = models.IntegerField()
    imagen_usuario = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.usuario.username
