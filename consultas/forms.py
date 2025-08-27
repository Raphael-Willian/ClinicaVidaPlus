# consultas/forms.py
from django import forms
from .models import Consulta
from datetime import time

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ["pacientes", "profissional", "data", "hora"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # se já tiver profissional e data informados, calcula horários livres
        if "profissional" in self.data and "data" in self.data:
            try:
                profissional_id = int(self.data.get("profissional"))
                data = self.data.get("data")
                from .models import Consulta  # evitar import circular
                from profissionais.models import Profissional
                from datetime import datetime

                profissional = Profissional.objects.get(pk=profissional_id)
                data = datetime.strptime(data, "%Y-%m-%d").date()

                # gera lista de horários (08h às 17h, de hora em hora)
                todos = [time(h, 0) for h in range(8, 18)]
                ocupados = Consulta.objects.filter(
                    profissional=profissional,
                    data=data
                ).values_list("hora", flat=True)

                livres = [h for h in todos if h not in ocupados]
                self.fields["hora"].widget = forms.Select(choices=[(h, h.strftime("%H:%M")) for h in livres])
            except Exception:
                pass  # se não conseguir processar, deixa o campo padrão
        else:
            # enquanto não escolher profissional e data, desabilita o campo hora
            self.fields["hora"].widget = forms.Select(choices=[])
            self.fields["hora"].disabled = True
