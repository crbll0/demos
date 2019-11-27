import logging
from odoo import api, models

_logger = logging.getLogger(__name__)


class TierDefinition(models.Model):
    _inherit = "tier.definition"

    @api.model
    def _get_tier_validation_model_names(self):
        res = super(TierDefinition, self)._get_tier_validation_model_names()
        res.append("sale.order")
        return res
    
    @api.multi
    def write(self, vals):
        for rec in self:
            if (getattr(rec, self._state_field) in self._state_from and
                    vals.get(self._state_field) in self._state_to):
                if rec.need_validation:
                    # try to validate operation
                    reviews = rec.request_validation()
                    rec._validate_tier(reviews)
                    if not self._calc_reviews_validated(reviews):
                        raise ValidationError(_(
                            "This action needs to be validated for at least "
                            "one record. \nPlease request a validation."))
                if rec.review_ids and not rec.validated:
                    raise ValidationError(_(
                        "A validation process is still open for at least "
                        "one record."))

            _logger.info(('estado :', getattr(rec, self._state_field) , 'en' , self._state_from, getattr(rec, self._state_field) in self._state_from ))
            _logger.info(('estado :', getattr(rec, self._state_field) , 'no en' , self._state_to, getattr(rec, self._state_field) not in (self._state_to +[self._cancel_state]) ))
            _logger.info(('_check_allow_write_under_validation :', self._check_allow_write_under_validation(vals)))
            #_logger.info((' :', ))
            #_logger.info((' :', ))
            #_logger.info((' :', ))
            if (rec.review_ids and getattr(rec, self._state_field) in
                    self._state_from and not vals.get(self._state_field) in
                    (self._state_to + [self._cancel_state]) and not
                    self._check_allow_write_under_validation(vals)):
                raise ValidationError(_("The operation is under validation."))
        if vals.get(self._state_field) in self._state_from:
            self.mapped('review_ids').unlink()
        return super(TierValidation, self).write(vals)
