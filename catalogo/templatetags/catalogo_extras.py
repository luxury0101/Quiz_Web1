from django import template


register = template.Library()


@register.filter
def cop(valor):
    """Formatea un precio como pesos colombianos, sin decimales."""
    return f"${valor:,.0f}".replace(",", ".")

