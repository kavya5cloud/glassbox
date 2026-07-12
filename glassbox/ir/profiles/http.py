"""HTTP profile for the Glassbox IR."""

from __future__ import annotations

from dataclasses import dataclass

from glassbox.ir.node import Node
from glassbox.ir.observation import Observation


@dataclass(frozen=True, slots=True)
class HTTPProfile:
    """Convert capture observations into neutral IR nodes."""

    name: str = "http"

    def transform(self, observations: tuple[Observation, ...]) -> tuple[Node, ...]:
        nodes: list[Node] = []
        for observation in observations:
            nodes.append(
                Node(
                    id=observation.id,
                    kind=self._node_kind(observation.kind),
                    occurred_at=observation.occurred_at,
                    attributes=observation.fields,
                    metadata=observation.metadata,
                )
            )
        return tuple(nodes)

    @staticmethod
    def _node_kind(kind: str) -> str:
        if kind == "http_request":
            return "http.request"
        if kind == "process_started":
            return "process.started"
        if kind == "process_finished":
            return "process.finished"
        return kind
