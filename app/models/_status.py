"""
Por que fazer uso de bit a bit?
Ele facilita quando deve-se comparar múltiplos valores de modo eficiente
"""

from enum import Enum

class Status(Enum):
    
    BLINDED = 0x01         # CEGO
    CHARMED = 0x02         # ENFEITIÇADO
    DEAFENED = 0x04        # SURDO
    FRIGHTENED = 0x08      # AMEDRONTADO
    GRAPPLED = 0x10        # AGARRADO
    INCAPACITATED = 0x20   # INCAPACITADO
    INVISIBLE = 0x40       # INVISÍVEL
    PARALYZED = 0x80       # PARALISADO
    PETRIFIED = 0x100      # PETRIFICADO
    POISONED = 0x200       # ENVENENADO
    PRONE = 0x400          # CAÍDO
    RESTRAINED = 0x800     # IMPEDIDO
    STUNNED = 0x1000       # ATORDOADO
    UNCONSCIOUS = 0x2000   # INCONSCIENTE
    
    IN_COMBAT = 0x4000     # EM COMBATE