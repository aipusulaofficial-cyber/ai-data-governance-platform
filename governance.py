from dataclasses import dataclass
@dataclass(frozen=True)
class Asset: id:str; owner:str; classification:str
class GovernanceError(Exception): pass
class Catalog:
 def __init__(self): self.assets={};self.edges={}
 def register(self,a):
  if not a.owner: raise GovernanceError("owner required")
  self.assets[a.id]=a
 def link(self,p,c):
  if p not in self.assets or c not in self.assets: raise GovernanceError("unknown asset")
  self.edges.setdefault(p,set()).add(c)
 def lineage(self,root):
  seen=set();stack=[root]
  while stack:
   x=stack.pop()
   if x in seen: continue
   seen.add(x);stack.extend(self.edges.get(x,()))
  return seen
class Policy:
 def check(self,a,allowed):
  if a.classification not in allowed: raise GovernanceError("classification denied")
  return True
