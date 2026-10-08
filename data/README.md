# Data

No datasets are stored in this repository yet. This page says how to handle them when an experiment needs them. See also [experiments/README.md](../experiments/README.md) and [.gitignore](../.gitignore).

## Small public fixtures

A fixture is a tiny public example used to show a file format or to exercise a loader. It may be committed when it contains no private information and is small enough to review in Git. A fixture is not a training set, a development set, or evidence about a model.

Suggested path: `data/fixtures/`. Create it with the first fixture.

## Training data

Training data is material used to teach a model. Record its provenance, review status, the case specification it came from, and a version identifier in the experiment folder. A narrative may be fictional. Speculative futures, claims of AI consciousness, and the inevitability of any particular future are not to be presented as established facts. Original synthetic text can draw on themes without copying novels.

Small reviewed training sets may be committed. Large ones stay outside Git. See below.

## Development cases

Development cases are used to refine tasks, prompts, scorers, and methods. Once a case has influenced those choices, it is development data. It is not a confirmation set.

Keep development cases in a versioned location named by the experiment, and point to that version from the protocol. Suggested path for material that is small and shareable: `data/development/`.

## Protected confirmation sets

A confirmation set is a fresh collection of cases held out after the relevant protocol is frozen. It is the evidence used for the pre-stated comparison.

Implementation work does not read confirmation data unless the research owner explicitly authorizes that access for a named task. If a result from the confirmation set leads to a change in training or prompts, that set becomes development data, and the study needs a new confirmation set.

Store confirmation data where access can actually be limited. A local copy, if one must exist on this machine, belongs under `data/confirmation/`. That path is listed in `.gitignore` so a copy is less likely to be committed. Ignoring the path is not an access control. A gitignore rule, a folder name, an agent role, or a separate agent session does not grant or withhold permission to read the files.

## Large external artifacts

Store large datasets, generated corpora, model weights, and checkpoints outside Git. In the experiment folder, record a versioned reference: storage location, identifier, date, and checksum. Do not commit the artifacts. Paths ignored for this reason include `data/external/`, `data/generated/`, `checkpoints/`, and `weights/`.

Credentials never belong in the repository.
