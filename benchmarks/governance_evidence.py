from governance_domain import Asset,evaluate
allowed=evaluate(Asset("a","alice","internal"),"confidential","alice"); denied=evaluate(Asset("b","alice","restricted"),"internal","bob"); report={"allowed":allowed.allowed,"denied":denied.allowed,"denied_reasons":denied.reasons}
if not allowed.allowed or denied.allowed or "owner_mismatch" not in denied.reasons or "classification_exceeds_request" not in denied.reasons: raise SystemExit(report)
print(report)
