Feature: Valid if exist one docker image in docker hub

    Scenario Outline: Searching for an existing docker image
        Given We have installed docker
        When We search <user>/<repository>:<tag>
        Then We get the image name

    Examples: ednx-distro
        | user    | repository            | tag          |
        | ednxops | distro-edunext-edxapp | vM.mango.2.0 |

    Examples: openedx
        | user    | repository | tag          |
        | edxops  | discovery  | lilac.master |

    Scenario Outline: Searching for an non-existing docker image
        Given We have installed docker
        When We search <user>/<repository>:<tag>
        Then We get an exeption

    Examples: ednx-distro
        | user    | repository            | tag          |
        | ednxops | distro-edunext-edxapp | queso |
